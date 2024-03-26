import pandas as pd
import glob

# 找到所有的 csv 檔案
csv_files = glob.glob('20240326/*.csv')

# 讀取每個 csv 檔案並將它們合併成一個 DataFrame
df_list = []
for filename in csv_files:
    df = pd.read_csv(filename, header=None)
    df.columns = ['time', 'gate_start', 'gate_end', 'type', 'travel_time', 'number']
    df_list.append(df)

# 合併所有的 DataFrame
df = pd.concat(df_list, ignore_index=True)

## 將結果另存成新的 CSV 檔案
df.to_csv('20240326/result.csv', index=False)


