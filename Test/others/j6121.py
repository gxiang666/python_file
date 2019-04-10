import requests
from bs4 import BeautifulSoup


def get_response(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) App"
                             "leWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"}
    response = requests.get(url, headers=headers)
    return response


def get_img_page(html):
    soup = BeautifulSoup(html, "html.parser")
    img_url_list = soup.find_all("img")
    global x
    for src_url in img_url_list:
        img_url = src_url.get("src")
        text = get_response(img_url).content
        with open("./imags/4/%d.jpg" % x, "wb") as f:
            f.write(text)
            x += 1


def main():
    url = "https://www.dbmeinv.com/"
    html = get_response(url).text
    get_img_page(html)


if __name__ == '__main__':
    try:
        x = 1
        main()
    except Exception as result:
        print(result)
