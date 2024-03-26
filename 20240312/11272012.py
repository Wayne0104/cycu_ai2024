import pandas as pd

# 讀取 Excel 文件
df = pd.read_excel('./20240312/112年1-10月交通事故簡訊通報資料.xlsx', engine='openpyxl')

# 過濾出國道名稱為國道一號且方向為南或南向的資料
filtered_df = df[(df['國道名稱'] == '國道1號') & (df['方向'].isin(['南', '南向']))]

# 取得前五筆資料
# filtered_df = filtered_df.head(500)

# 統計每個里程的次數
result = filtered_df['里程'].value_counts().sort_index()

# 列出里程及其發生次數
for mileage, count in result.items():
    print(f'里程：{mileage}, 發生次數：{count}')

# 找出次數最多的里程
max_mileage = result.idxmax()
print(f'次數最多的里程為：{max_mileage}')

# 輸出到 Excel 文件
result.to_excel('output.xlsx')

import matplotlib.pyplot as plt

# 畫出柱狀圖
result.plot(kind='bar', title='國道一號南向交通事故里程統計')

# 中文顯示
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 顯示較少的x軸標籤 (每隔100個顯示一次)
plt.xticks(range(0, len(result), 50), result.index[::50], rotation=45)

plt.show()
