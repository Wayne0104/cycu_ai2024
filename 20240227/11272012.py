# print("Hello, World!")

import feedparser

# 設定要爬取的網址
url = "https://news.pts.org.tw/xml/newsfeed.xml"

# 使用 feedparser 解析 RSS feed
feed = feedparser.parse(url)

# 輸出 feed 的標題和項目數量
print("Feed title:", feed.feed.title)
print("Number of entries:", len(feed.entries))

# 遍歷每一個 'entry'
for entry in feed.entries:
    # 輸出該項目的標題
    print(entry.title)

    #印出 summary
    print(entry.summary)

    #印出 link 
    print(entry.link)

    #印出 分隔線
    print("-" * 80)

    #幫我找是否有含桃園的新聞標題
    if "桃園" in entry.title:
        print("桃園新聞:", entry.title)
#幫我把列印出之標題依序存入一個excel檔案，檔名為11272012.xlsx
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "News"
sheet["A1"] = "Title"
sheet["B1"] = "Summary"
sheet["C1"] = "Link"
#設定行數
row = 2
# 遍歷每一個 'entry'
for entry in feed.entries:
    sheet["A" + str(row)] = entry.title
    sheet["B" + str(row)] = entry.summary
    sheet["C" + str(row)] = entry.link
    row += 1
#存檔
wb.save("11272012.xlsx")
#關閉檔案
wb.close()
#印出完成
print("Done!")
# Path: 20240227/11272012.py


