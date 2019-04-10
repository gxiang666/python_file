import requests
from bs4 import BeautifulSoup

url = "http://tu.duowan.com/m/bizhi"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch"
                         "rome/67.0.3396.79 Safari/537.36"}
r = requests.get(url, headers=headers)
r.encoding = "utf-8"
# print(r.text)
html = r.text
soup = BeautifulSoup(html, "html.parser")
a_tag_lsit = soup.find_all("a", target="_blank")
# print(a_tag_lsit)
page_url = []
for a_tag in a_tag_lsit:
    img_url = a_tag.find_all("img")
    if img_url:
        page_url.append(a_tag)
        # print(page_url)
        # a_url = a_tag.get("href")
        # print(a_url)
page_url.pop(0)
# for i in page_url:
#     a_url = i.get("href")
#     # print(a_url)
#     response = requests.get(a_url, headers=headers).text
#     print(response)
# res = requests.get(page_url[0], headers=headers).text
print(page_url[0])



