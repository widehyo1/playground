import sys
import sqlite3
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import plotly.graph_objects as go

DB_PATH = "~/finance.db"


def get_args():
    """CLI 인자 처리: 날짜가 없으면 오늘 날짜 사용"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return datetime.now().strftime("%Y-%m-%d")


def parse_portpolio(row, apply_fx=True):
    date, ticker, name, amount, price, currency, usd_per_krw, account, type_ = row
    price = float(price)
    value = amount * price

    if currency == "USD" and apply_fx:
        value *= usd_per_krw

    type_dict = {
        "연금저축": "연금",
        "IRP": "연금",
        "퇴직연금": "연금",
        "일반계좌": "입출금계좌",
        "직투계좌": "직투계좌",
        "ISA": "ISA",
    }

    return {
        "currency": currency,
        "name": name,
        "type": type_dict[type_],
        "account": account,
        "value": value,
    }


def generate_currency_rows(dbpath, date, conn, currency):
    cur = conn.cursor()
    yield from (
        parse_portpolio(row, apply_fx=False)
        for row in cur.execute(f"select * from portpolio where date = '{date}'")
        if currency == row[5]
    )


def get_krw_usd_rows(dbpath=DB_PATH, date=None):
    if date is None:
        date, _timestamp = datetime.isoformat(datetime.now()).split("T")
    finance_db_path = Path(dbpath).expanduser()
    with sqlite3.connect(finance_db_path) as conn:
        rows_krw = list(generate_currency_rows(dbpath, date, conn, "KRW"))
        rows_usd = list(generate_currency_rows(dbpath, date, conn, "USD"))
    return rows_krw, rows_usd


def make_sankey(rows, domain_x, title, unit):
    nodes = set()
    links = defaultdict(float)

    total_value = sum(r["value"] for r in rows)

    for r in rows:
        nodes.add(f"TYPE:{r['type']}")
        nodes.add(f"ACC:{r['account']}")
        nodes.add(f"NAME:{r['name']}")

        v = r["value"]
        links[(f"TYPE:{r['type']}", f"ACC:{r['account']}")] += v
        links[(f"ACC:{r['account']}", f"NAME:{r['name']}")] += v

    node_list = list(nodes)
    node_index = {n: i for i, n in enumerate(node_list)}

    source, target, value, ratio = [], [], [], []
    for (s, t), v in links.items():
        source.append(node_index[s])
        target.append(node_index[t])
        value.append(v)
        ratio.append(v / total_value)

    sankey = go.Sankey(
        name=title,
        domain=dict(x=domain_x, y=[0, 1]),
        node=dict(
            pad=15,
            thickness=15,
            label=[
                n.replace("TYPE:", "").replace("ACC:", "").replace("NAME:", "")
                for n in node_list
            ],
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            customdata=ratio,
            hovertemplate=(
                "값: %{value:,.0f} " + unit + "<br>"
                "비율: %{customdata:.1%}"
                "<extra></extra>"
            ),
        ),
    )
    # 하단 총합 annotation
    annotation = dict(
        x=sum(domain_x) / 2,
        y=0.03,
        xref="paper",
        yref="paper",
        text=f"<b>Total: {total_value:,.0f} {unit}</b>",
        showarrow=False,
        font=dict(size=13),
    )

    return sankey, annotation


def get_types_ranking():
    return {"ISA": 1, "연금": 2, "입출금계좌": 3, "직투계좌": 4}


def get_accounts_ranking():
    return {
        "NH ISA": 1,
        "NH IRP": 2,
        "삼성증권 연금저축": 3,
        "IBK 퇴직연금 DC": 4,
        "IBK": 5,
        "NH": 6,
        "NH CMA": 7,
    }


def get_name_ranking():
    return {
        "KODEX 미국나스닥100": 1,
        "자동운용상품(고유계정대)": 2,
        "삼성신종종류형MMF제4호-CP": 3,
        "TIGER 미국필라델피아반도체나스닥": 4,
        "프로셰어즈 QQQ 2배 ETF": 5,
        "프로셰어즈 QQQ 3배 ETF": 6,
        "디렉시온 MSCI 한국 3배 ETF": 7,
        "아이셰어즈 0-3개월 미국 국책 ETF": 8,
        "현금성자산": 99,
        "원": 100,
        "달러": 101,
    }


def make_parallel_sets(rows, domain_x, title, unit):
    """Sankey 대신 Parallel Categories(Parallel Sets)를 사용하는 함수"""
    if not rows:
        return None, None

    # 1. 딕셔너리 정의 (속도 향상을 위해 함수 밖으로 빼는 것을 추천)
    type_ranking = get_types_ranking()
    account_ranking = get_accounts_ranking()
    name_ranking = get_name_ranking()

    # 2. 전체 행(row)을 정렬 (우선순위: Type > Account > Name)
    # 딕셔너리에 없는 키가 올 경우를 대비해 get(k, 999) 사용
    sorted_rows = sorted(
        rows,
        key=lambda r: (
            type_ranking.get(r["type"], 999),
            account_ranking.get(r["account"], 999),
            name_ranking.get(r["name"], 999),
        ),
    )

    # 3. 정렬된 상태에서 리스트 추출 (이래야 데이터 관계가 유지됨)
    types = [r["type"] for r in sorted_rows]
    accounts = [r["account"] for r in sorted_rows]
    names = [r["name"] for r in sorted_rows]
    values = [r["value"] for r in sorted_rows]

    total_value = sum(values)

    parcats = go.Parcats(
        domain=dict(x=domain_x, y=[0.1, 1.0]),
        dimensions=[
            dict(label="Type", values=types),
            dict(label="Account", values=accounts),
            dict(label="Asset", values=names),
        ],
        counts=values,
        hoverinfo="count+probability",
        labelfont=dict(size=14),
        tickfont=dict(size=12),
        arrangement="freeform",
    )

    annotation = dict(
        x=sum(domain_x) / 2,
        y=0.03,
        xref="paper",
        yref="paper",
        text=f"<b>{title}<br>Total: {total_value:,.0f} {unit}</b>",
        showarrow=False,
        font=dict(size=13),
    )

    return parcats, annotation


if __name__ == "__main__":
    target_date = get_args()
    print(f"Target Date: {target_date}")

    try:
        rows_krw, rows_usd = get_krw_usd_rows(DB_PATH, target_date)
    except Exception as e:
        print(f"에러 발생: {e}")
        sys.exit(1)

    fig = go.Figure()
    annotations = []

    # 시각화 생성 (Parallel Sets)
    pc_krw, ann_krw = make_parallel_sets(rows_krw, [0.0, 0.48], "KRW Portfolio", "₩")
    if pc_krw:
        fig.add_trace(pc_krw)
        annotations.append(ann_krw)

    pc_usd, ann_usd = make_parallel_sets(rows_usd, [0.52, 1.0], "USD Portfolio", "$")
    if pc_usd:
        fig.add_trace(pc_usd)
        annotations.append(ann_usd)

    fig.update_layout(
        title_text=f"Portfolio Parallel Sets ({target_date})",
        font=dict(family="Noto Sans KR", size=12),
        annotations=annotations,
        margin=dict(t=100, b=50, l=50, r=50),
    )

    fig.show()

    # output_path = Path(f"portfolio_{target_date}.png")
    # fig.write_image(str(output_path), engine="kaleido", width=1200, height=800)
    # fig.write_image(str(output_path.with_suffix(".pdf")), engine="kaleido")
    # print(f"저장 완료: {output_path} 및 PDF")
