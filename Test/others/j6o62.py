import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.bilibili.com/account/history", timeout=30)
# print(r.status_code)
demo = r.text
# print(demo)
soup = BeautifulSoup(demo, "html.parser")
text = soup.prettify()


with open("./txt/text.txt", "w") as f:
    f.write(text)
