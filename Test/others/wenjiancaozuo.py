import os
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.bilibili.com/account/history/", timeout=30)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
text = soup.prettify()


os.mkdir("D:/xgx")

with open("D:/xgx/text.txt", "w") as f:
    f.write(text)
    f.close()
