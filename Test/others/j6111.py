import requests
from bs4 import BeautifulSoup


def get_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chro"
                             "me/67.0.3396.79 Safari/537.36",
               "Referer": "https: // www.baidu.com / link?url = ax3ZJYUVIXjnnJiu6GejZQCsh4j_ork5s8AE - AomXcsuY - jHr"
                          "rL1VjRJwz52olH8 & wd = & eqid = a0fdee3a0002375f000000035b1e88ae"}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    r.encoding = r.apparent_encoding
    r.close()
    return r


def get_url(html):
    suop = BeautifulSoup(html, "html.parser")
    imgs_list = soup.find_all("img")
    global x
    for img in imgs_list:
        img_url = img.get("src")
        with open("./imags/3/%d" % x, "wb") as f:
            f.write(get_url(img_url).content)


def main():
    x = 1
    url = "http://www.meizitu.com"
    get_page(url)
