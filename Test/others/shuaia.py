import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "http://www.shuaia.net/e/tags/?tagname=%E5%8A%A8%E6%BC%AB"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chro"
                             "me/67.0.3396.79 Safari/537.36"}
    r = requests.get(url=url, headers=headers)
    r.encoding = "utf-8"
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all(class_="item-img")
    for tag in tags:
