# 取原始碼
import bs4
import urllib.request as req


def getData(url):
    # 加一個headers 偽裝人類
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "cookie": "over18=1"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # 解析原始碼
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
            # 抓取上一頁的連結
    nextLink = root.find("a", string="‹ 上頁")  # 找到內文是 ‹ 上頁 的 a 標籤
    return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageURL="https://ww.ptt.cc"+getData(pageURL)
    count+=1
