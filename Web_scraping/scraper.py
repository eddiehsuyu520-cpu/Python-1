import requests
from bs4 import BeautifulSoup

# 目標網站：quotes.toscrape.com（專為爬蟲練習設計的公開網站）
URL = "http://quotes.toscrape.com"

def scrape_quotes(url):
    print(f"正在爬取：{url}\n")

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"請求失敗，狀態碼：{response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    print(f"{'=' * 60}")
    for i, quote in enumerate(quotes, 1):
        text   = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags   = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

        print(f"[{i}] {text}")
        print(f"    作者：{author}")
        print(f"    標籤：{', '.join(tags)}")
        print(f"{'=' * 60}")

    # 取得下一頁連結
    next_btn = soup.find("li", class_="next")
    if next_btn:
        next_url = URL + next_btn.find("a")["href"]
        print(f"\n下一頁：{next_url}")

scrape_quotes(URL)
