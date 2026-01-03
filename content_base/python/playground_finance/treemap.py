import sqlite3
from pathlib import Path
from datetime import datetime

import plotly.express as px
import pandas as pd

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

def draw_treemap(rows, depth1_key, title):
    df = pd.DataFrame(rows)

    fig = px.treemap(
        df,
        path=[depth1_key, "name"],
        values="value",
        title=depth1_key
    )

    fig.update_layout(
        font=dict(
            family="Noto Sans KR",
            size=12
        )
    )

    fig.show()

finance_db_path = Path('~/finance.db').expanduser()

rows = []
with sqlite3.connect(finance_db_path) as conn:
    cur = conn.cursor()
    for row in cur.execute("select * from portpolio"):
        rows.append(parse_portpolio(row))


# draw_treemap(
#     rows,
#     depth1_key="currency",
#     title="통화별 자산 구성 (Currency → Name)"
# )


# draw_treemap(
#     rows,
#     depth1_key="type",
#     title="계좌유형별 자산 구성 (Type → Name)"
# )


draw_treemap(
    rows,
    depth1_key="account",
    title="계좌별 자산 구성 (Account → Name)"
)
