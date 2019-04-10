import requests
from bs4 import BeautifulSoup

url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word" \
      "=%D7%C0%C3%E6%B1%DA%D6%BD%B6%AF%C2%FE&fr=ala&ala=1&pos" \
      "=0&alatpl=wallpaper&oriquery=%E6%A1%8C%E9%9D%A2%E5%A3%81%E7%BA%B8%E5%8A%A8%E6%BC%AB"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537."
                         "36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
r = requests.get(url, headers=headers, timeout=30)
# print(r.status_code)
demo = r.content
soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())
pic_url_list = soup.find_all("img<img class="*" data-imgurl="http://img3.imgtn.bdimg.com/it/u=467368505,422355496&amp;fm=27&amp;gp=0.jpg" src="http://img3.imgtn.bdimg.com/it/u=467368505,422355496&amp;fm=27&amp;gp=0.jpg" style="background-color: rgb(219, 191, 178); width: 281px; height: 158px;">")

for i in pic_url_list:
    print(i)
