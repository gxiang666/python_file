import requests
from bs4 import BeautifulSoup

url = "https://www.dbmeinv.com/?pager_offset=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/53"
                         "7.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
r = requests.get(url=url, headers=headers)
print(r.status_code)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
pics = soup.find_all("img")
x = 0
for pic in pics:
    link = pic.get("src")


