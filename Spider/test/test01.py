# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
url = "https://www.qiushibaike.com/text/"
response = requests.get(url, headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")
print(soup)

