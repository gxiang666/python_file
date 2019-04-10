import requests
from bs4 import BeautifulSoup
url = "https://www.dbmeinv.com/?pager_offset=3"


def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/53"
                             "7.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    r = requests.get(url=url, headers=headers)
    return r


def get_img(rsp):
    html = rsp.text
    soup = BeautifulSoup(html, "html.parser")
    pics = soup.find_all("img")
    x = 0
    for pic in pics:
        link = pic.get("src")
        print(link)
        img_html = get_html(link)
        ph = img_html.content
        file = open("imags/%s.jpg" % x, "wb")
        file.write(ph)
        file.close()
        x += 1


try:
    rsp = get_html(url)
    get_img(rsp)
except Exception as result:
    print(result)

