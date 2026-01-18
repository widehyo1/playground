import pandas as pd
import re

df1 = pd.read_csv('nh.csv')
df2 = pd.read_csv('samsumg.csv')

# 2. 파일 1 정리
journal1 = pd.DataFrame({
    'date': pd.to_datetime(df1['실거래일자']),
    'symbol': df1['종목명'].fillna('현금'),
    'type': df1['거래유형'],
    'quantity': df1['수량'],
    'price': df1['단가'],
    'amount': df1['정산금액']
})

# 3. 파일 2 정리 (숫자 전처리 필요)
def clean_number(x):
    if pd.isna(x) or x == "": return 0
    # 쉼표 제거 및 괄호를 마이너스 기호로 변환 (예: (10) -> -10)
    s = str(x).replace(',', '')
    if '(' in s:
        s = '-' + s.replace('(', '').replace(')', '')
    return float(s)

journal2 = pd.DataFrame({
    'date': pd.to_datetime(df2['거래일자'].str.replace('.', '-')),
    'symbol': df2['거래내용'].fillna('현금'),
    'type': df2['거래명'],
    'quantity': df2['잔고수량'], # 혹은 '감소/증가' 필드에서 파싱 가능
    'price': df2['거래단가'].apply(clean_number),
    'amount': df2['증가'].apply(clean_number) - df2['감소'].apply(clean_number)
})

# 4. 통합 및 저장
final_journal = pd.concat([journal1, journal2], ignore_index=True)
final_journal = final_journal.sort_values(by='date')

# 최종 결과 저장
final_journal.to_csv('trading_journal.csv', index=False, encoding='utf-8-sig')
print("통합 완료: trading_journal.csv")
