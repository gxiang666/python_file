import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.dbmeinv.com/?pager_offset=1", timeout=30)
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())
text = soup.prettify("utf-8")
with open("./txt/content.txt", "w") as f:
    f.write(str(text))


