import pandas as pd
import requests
from bs4 import BeautifulSoup


# https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx
url = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all table elements on the page
tables = soup.find_all("table")

# Convert each table to a pandas DataFrame
dataframes = []
for table in tables:
    df = pd.read_html(str(table))[0]
    dataframes.append(df)

# Print the resulting DataFrames
for i, df in enumerate(dataframes):
    print(f"DataFrame {i+1}:")
    print(df)
    print()

# Save the DataFrames (df2) to CSV files
dataframes[1].to_csv("oil_prices.csv", index=False)

import matplotlib.pyplot as plt

# 設定圖表文字為中文
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

# df2 只保留前5個欄位的資料
df2 = dataframes[1].iloc[:, :5]

# 去除值是NaN的資料
df2 = df2.dropna()

# 把第一欄的資料型態 轉成 datetime
df2[df2.columns[0]] = pd.to_datetime(df2[df2.columns[0]])

# 設定圖表標題為 "CPC 油價走勢"
plt.title("CPC 油價走勢")

# 設定 x 軸標題為 "日期"
plt.xlabel("日期")

# 設定 y 軸標題為 "油價"
plt.ylabel("油價")

# 使用 matplotlib x,y 折線圖 , x 軸是日期 , 後面四個欄位是 油價 ，分別是 92無鉛汽油,95無鉛汽油,98無鉛汽油,超級柴油，並設定線條顏色為 紅色 黃色 淡藍色 綠色，設定圖例位置在左上角
plt.plot(df2[df2.columns[0]], df2[df2.columns[1]], label='92無鉛汽油', color='red')
plt.plot(df2[df2.columns[0]], df2[df2.columns[2]], label='95無鉛汽油', color='yellow')
plt.plot(df2[df2.columns[0]], df2[df2.columns[3]], label='98無鉛汽油', color='lightblue')
plt.plot(df2[df2.columns[0]], df2[df2.columns[4]], label='超級柴油', color='green')
plt.legend(loc='upper left')
plt.show()




















