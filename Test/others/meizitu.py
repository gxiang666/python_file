import requests
from bs4 import BeautifulSoup


def get_rsp():

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleW"
                         "ebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    r = requests.get("http://www.meizitu.com/", headers)
    return r


def get_html(html):
    soup = BeautifulSoup(html, "html.parser")
    img_list = soup.find_all("a")
    for img in img_list:
        print(img.get("href"))


def main():
    html = get_rsp()
    get_html(html=html)


main()
