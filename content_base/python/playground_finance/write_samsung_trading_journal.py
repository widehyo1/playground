from pathlib import Path
import pandas as pd

XLS_PATH_STR = (
    "/home/widehyo/gitclone/playground/content_base/python/playground_finance/xls"
)
xls_path = Path(XLS_PATH_STR)

samsung_files = ["isa_samsung.xlsx"]

df = pd.read_excel(xls_path / "isa_samsung.xlsx", skiprows=2)
df.to_csv('samsung_trading_journal.csv', index=False, encoding='utf-8')
