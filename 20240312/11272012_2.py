import pandas as pd
from datetime import datetime

# 讀取 Excel 文件
df = pd.read_excel('112年1-10月交通事故簡訊通報資料.xlsx', engine='openpyxl')

# 篩選欄位為國道1號的資料
df = df[df['國道名稱'] == '國道3號']

# 篩選方向為南及南向的資料
df = df[(df['方向'] == '北') | (df['方向'] == '北向')]

# 將文件中的 年 月 日 時 分 欄位合併成一個欄位，轉換為日期格式
df['事件開始'] = df['年'].astype(str) + '-' + df['月'].astype(str) + '-' + df['日'].astype(str) + ' ' + df['時'].astype(str) + ':' + df['分'].astype(str)

# 將文件中的 年 月 日 事件排除 欄位合併成一個欄位，轉換為日期格式
df['事件結束'] = df['年'].astype(str) + '-' + df['月'].astype(str) + '-' + df['日'].astype(str) + ' ' + df['事件排除'].astype(str)

# 計算 事件開始 距離 2023年1月1日0時0分0秒 的秒數
df['事件開始'] = (pd.to_datetime(df['事件開始']) - datetime(2023, 1, 1, 0, 0, 0)).dt.total_seconds()

# 計算 事件結束 距離 2023年1月1日0時0分0秒 的秒數
df['事件結束'] = (pd.to_datetime(df['事件結束']) - datetime(2023, 1, 1, 0, 0, 0)).dt.total_seconds()

# 利用 matplotlib 繪製圖表
import matplotlib.pyplot as plt

# 畫出範圍橫條圖
for index, row in df.iterrows():
    plt.plot([row['事件開始'], row['事件結束']], [row['里程'], row['里程']])
    
#  標題為 '國道1號 南向 交通事故' 加上 學號 : 11272012
plt.title('國道3號 北向 交通事故 學號 : 11272012')

# 設定中文顯示
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

# 儲存圖表
plt.savefig('0312_3.png')

# 顯示圖表
plt.show()





