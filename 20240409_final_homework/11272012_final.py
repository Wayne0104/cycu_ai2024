import pandas as pd

# 讀取 CSV 檔案
data1 = pd.read_csv( './20240409_final_homework/地震活動彙整.csv', encoding='big5' )

# 選取 '經度', '緯度', '規模' 欄位
selected_data = data1[[ '地震時間', '經度', '緯度', '規模', '深度', '位置' ]]

# 顯示前五行資料
print(selected_data)

import pandas as pd

# 假設 '地震時間' 是一個形如 '2022-01-01 12:34:56' 的字串
selected_data.loc[:, '地震時間'] = pd.to_datetime(selected_data['地震時間'], format='%Y/%m/%d %H:%M')

import folium

# 建立台灣地圖
taiwan_map = folium.Map(location=[23.6978, 120.9605], zoom_start=7)

import matplotlib.pyplot as plt
import matplotlib.colors as colors
from folium.plugins import TimestampedGeoJson

# 建立一個空的 GeoJSON 物件
data = { "type": "FeatureCollection", "features": [] }

# 建立一個顏色映射
cmap = plt.get_cmap('gnuplot')  # 更改此處的 'Spectral' 為您想要的顏色映射

# 遍歷 selected_data 中的每一行
for index, row in selected_data.iterrows():

    # 根據地震規模設定顏色
    rgba_color = cmap(row['規模'] / selected_data['規模'].max())
    
    # 將 RGBA 格式的顏色轉換為十六進制碼
    color = colors.rgb2hex(rgba_color)

    # 建立一個新的 feature
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row['經度'], row['緯度']]
        },
        "properties": {
            "time": row['地震時間'].isoformat(),  # 注意：時間必須是 ISO 格式的字串
            "style": {"color" : color},
            "icon": "circle",
            "iconstyle":{
                "fillColor": color,
                "fillOpacity": 0.6,
                "stroke": "true",
                "radius": row['規模']*2
            },
            "popup": f"地震時間：{row['地震時間']}<br>規模：{row['規模']}<br>經度：{row['經度']}<br>緯度：{row['緯度']}<br>位置：{row['位置']}"
        }
    }

    # 將新的 feature 添加到 GeoJSON 物件中
    data["features"].append(feature)

# 將 GeoJSON 物件添加到地圖中
TimestampedGeoJson(
    data,
    period="PT1H",  # 每一步的時間間隔，這裡設定為 1 小時
    add_last_point=True,  # 是否在動畫結束時添加一個靜態的點
).add_to(taiwan_map)

# 儲存地圖
taiwan_map.save('taiwan_map.html')

