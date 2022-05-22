import FinanceDataReader as fdr

# 한국거래소 상장종목 전체
df_krx = fdr.StockListing('KRX')
print(df_krx.head())

# KRX stock symbol list
stocks = fdr.StockListing('KRX') # 코스피, 코스닥, 코넥스 전체
stocks = fdr.StockListing('KOSPI') # 코스피
stocks = fdr.StockListing('KOSDAQ') # 코스닥
stocks = fdr.StockListing('KONEX') # 코넥스

# NYSE, NASDAQ, AMEX stock symbol list
stocks = fdr.StockListing('NYSE')   # 뉴욕거래소
stocks = fdr.StockListing('NASDAQ') # 나스닥
stocks = fdr.StockListing('AMEX')   # 아멕스


df = fdr.DataReader('215600', '2018')
print(df.head(10))
