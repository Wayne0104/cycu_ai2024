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
    

