from pathlib import Path
import pandas as pd

XLS_PATH_STR = (
    "/home/widehyo/gitclone/playground/content_base/python/playground_finance/xls"
)
xls_path = Path(XLS_PATH_STR)

nh_files = [
    ("acc1_rec.xls", '203-01-446938'),
    ("acc_irp_nh.xls", '203-07-446938'),
    ("acc_isa_nh.xls", '210-02-881677')
]

merge_nh_files = [
    "acc2_rec1.xls",
    "acc2_rec2.xls",
]

merge_dfs = [pd.read_html(xls_path / nh_file)[0] for nh_file in merge_nh_files]
acc2_df = pd.concat(merge_dfs)
acc2_df['계좌번호'] = '203-02-446938'

def get_dfs(nh_files):
    dfs = []
    for nh_file, acc_num in nh_files:
        df = pd.read_html(xls_path / nh_file)[0]
        df['계좌번호'] = acc_num
        dfs.append(df)
    return dfs

dfs = get_dfs(nh_files)
dfs.append(acc2_df)
nh_df = pd.concat(dfs)

nh_df.to_csv('nh_trading_journal.csv', index=False, encoding='utf-8')
