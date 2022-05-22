import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/item/main.nhn?code=005930"

samsung_electronic = requests.get(URL)
html = samsung_electronic.text
soup = BeautifulSoup(html, 'html.parser')
finance_html = soup.select('div.section.cop_analysis div.sub_section')[0]

th_data = [item.get_text().strip() for item in finance_html.select('thead th')]
annual_date = th_data[3:7]
quarter_date = th_data[7:13]

print(annual_date)

finance_index = [item.get_text().strip() for item in finance_html.select('th.h_th2')][3:]

print(finance_index)

finance_data = [item.get_text().strip() for item in finance_html.select('td')]

print(finance_data)

finance_data = np.array(finance_data)
finance_data.resize(len(finance_index), 10)

finance_date = annual_date + quarter_date
finance = pd.DataFrame(data=finance_data[0:,0:], index=finance_index, columns=finance_date)

annual_finance = finance.iloc[:, :4]
quarter_finance = finance.iloc[:, 4:]

print(annual_finance)
