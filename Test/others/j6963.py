import requests
from bs4 import BeautifulSoup


x = 0


def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like G"
                             "ecko) Chrome/67.0.3396.62 Safari/537.36"}
    r = requests.get(url, headers=headers, timeout=30)
    print(r.status_code)
    r.encoding = r.apparent_encoding
    return r.content


def get_pics(html):
    soup = BeautifulSoup(html, "html.parser")
    pics_list = soup.find_all("img")
    global x
    for pic in pics_list:
        pic_url = pic.get("src")
        pic_html = get_html(pic_url)
        with open("./imags/%d.jpg" % x, "wb") as f:
            f.write(pic_html)
            x += 1


def main():
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        url = "https://www.dbmeinv.com/?pager_offset={}".format(i)
        html = get_html(url=url)
        get_pics(html=html)


try:
    main()
except Exception as result:
    print(result)


