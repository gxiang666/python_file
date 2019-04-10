import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Ch"
                  "rome/67.0.3396.62 Safari/537.36"
   }
url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&" \
      "fmq=1528642788130_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=%E" \
      "6%A1%8C%E9%9D%A2%E5%A3%81%E7%BA%B8%E5%8A%A8%E6%BC%AB"
r = requests.get(url, headers)
r.encoding = r.apparent_encoding
print(r.text)

