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

    # 왼쪽: KRW
    sankey_krw, ann_krw = make_sankey(
        rows_krw, domain_x=[0.0, 0.48], title="KRW Portfolio", unit="₩"
    )
    fig.add_trace(sankey_krw)
    annotations.append(ann_krw)

    # 오른쪽: USD
    sankey_usd, ann_usd = make_sankey(
        rows_usd, domain_x=[0.52, 1.0], title="USD Portfolio", unit="$"
    )
    fig.add_trace(sankey_usd)
    annotations.append(ann_usd)

    fig.update_layout(
        title_text="Portfolio Value Flow (KRW vs USD)",
        font=dict(family="Noto Sans KR", size=12),
        annotations=annotations,
    )

    output_path = Path(f"portfolio_{target_date}.png")
    fig.write_image(str(output_path), engine="kaleido", width=1200, height=800)
    fig.write_image(str(output_path.with_suffix('.pdf')), engine="kaleido")
    print(f"저장 완료: {output_path} 및 PDF")
