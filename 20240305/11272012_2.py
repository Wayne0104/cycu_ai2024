import pandas as pd
import requests
from bs4 import BeautifulSoup

# https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx
# https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx

# Define the URLs
url1 = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
url2 = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx"

# Send HTTP GET requests to the URLs
response1 = requests.get(url1)
response2 = requests.get(url2)

# Parse the HTML content
soup1 = BeautifulSoup(response1.content, "html.parser")
soup2 = BeautifulSoup(response2.content, "html.parser")

# Find the table elements
table1 = soup1.find_all("table")
table2 = soup2.find_all("table")

# Convert the tables to pandas dataframes
df1 = pd.read_html(str(table1))[1]
df2 = pd.read_html(str(table2))[1]

# Print the dataframes
print("Dataframe 1:")
print(df1)
print("\nDataframe 2:")
print(df2)

# 將 df2 的資料接在 df1 後面，並只保留前五欄的資料
df = pd.concat([df1, df2], ignore_index=True).iloc[:, :5]

# Save the combined dataframe to a CSV file
df.to_csv("oil_prices.csv", index=False)

import matplotlib.pyplot as plt

# 將調價日期的資料型態轉成 datetime
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]], errors='coerce')

# 移除含有 NaN 值的行
df = df.dropna()

# 將圖表文字設定為中文
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

# 設定圖表標題為 "CPC 油價走勢"
plt.title("CPC 油價走勢")

# 設定 x 軸標題為 "日期"
plt.xlabel("日期")

# 設定 y 軸標題為 "油價"
plt.ylabel("油價")


# 使用 matplotlib x,y 折線圖 , x 軸是日期 , 後面四個欄位是 油價 ，分別是 92無鉛汽油,95無鉛汽油,98無鉛汽油,超級柴油，並設定線條顏色為 紅色 黃色 淡藍色 綠色，設定圖例位置在左上角
plt.plot(df[df.columns[0]], df[df.columns[1]], label='92無鉛汽油', color='red')
plt.plot(df[df.columns[0]], df[df.columns[2]], label='95無鉛汽油', color='yellow')
plt.plot(df[df.columns[0]], df[df.columns[3]], label='98無鉛汽油', color='lightblue')
plt.plot(df[df.columns[0]], df[df.columns[4]], label='超級柴油', color='green')

# 顯示圖例
plt.legend(loc='upper left')

# 顯示圖表
plt.show()
