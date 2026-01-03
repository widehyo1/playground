import sqlite3
from pathlib import Path
from datetime import datetime
import plotly.graph_objects as go

def parse_portpolio(row):
    date, ticker, name, amount, price, currency, usd_per_krw, account, type_ = row
    date = datetime.fromisoformat(date)
    price = float(price)
    value = amount * price
    if currency == "USD":
        value = value * usd_per_krw
    type_dict = {}
    type_dict["연금저축"] = "연금"
    type_dict["IRP"] = "연금"
    type_dict["퇴직연금"] = "연금"
    type_dict["일반계좌"] = "입출금계좌"
    type_dict["직투계좌"] = "직투계좌"
    type_ = type_dict[type_]

    return {
        "currency": currency,
        "name": name,
        "type": type_,
        "account": account,
        "value": value
    }

finance_db_path = Path('~/finance.db').expanduser()

rows = []
with sqlite3.connect(finance_db_path) as conn:
    cur = conn.cursor()
    for row in cur.execute("select * from portpolio"):
        rows.append(parse_portpolio(row))

# 모든 노드 수집
nodes = set()

for r in rows:
    nodes.add(f"CUR:{r['currency']}")
    nodes.add(f"NAME:{r['name']}")
    nodes.add(f"TYPE:{r['type']}")
    nodes.add(f"ACC:{r['account']}")

node_list = list(nodes)
node_index = {n: i for i, n in enumerate(node_list)}

from collections import defaultdict

links = defaultdict(float)

for r in rows:
    v = r["value"]

    links[(f"TYPE:{r['type']}", f"ACC:{r['account']}")] += v
    links[(f"ACC:{r['account']}", f"NAME:{r['name']}")] += v
    links[(f"NAME:{r['name']}", f"CUR:{r['currency']}")] += v

source = []
target = []
value = []

for (s, t), v in links.items():
    source.append(node_index[s])
    target.append(node_index[t])
    value.append(v)

fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=15,
        label=[n.replace("TYPE:", "")
                .replace("ACC:", "")
                .replace("NAME:", "")
                .replace("CUR:", "")
               for n in node_list],
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
    )
))

fig.update_layout(
    title_text="Portfolio Value Flow (Type → Account → Name → Currency)",
    font=dict(family="Noto Sans KR", size=12)
)

fig.show()
