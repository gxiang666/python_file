import re

import requests


def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch"
                             "rome/68.0.3440.15 Safari/537.36"}
    r = requests.get(url=url, headers=headers)
    r.encoding = "utf-8"
    return r


def get_img_url_list(url):
    html = download(url).text
    regex = r'<a class="item-img" target="_blank" href="(.*?)">'
    url_list = re.findall(regex, html, re.S)
    return url_list


def save_img(img_item_url):
    html = download(img_item_url).text
    regex = r'<p style="text-align: center;">&nbsp;<img src="(.*?)" alt=".*?" width=".*?" height=".*?" /></p>'
    img_url_lsit = re.findall(regex, html, re.S)
    global x
    for img_url in img_url_lsit:
        com_url = 'http://www.shuaia.net' + img_url
        text = download(com_url).content
        print("下载")
        with open("./imgs/%d.jpg" % x, "wb") as f:
            f.write(text)
            x += 1


def main(url):
    img_url_item_list = get_img_url_list(url)
    print(len(img_url_item_list))
    for img_item_url in img_url_item_list:
        save_img(img_item_url)


if __name__ == '__main__':
    x = 1
    for i in range(140):
        start_url = "http://www.shuaia.net/e/tags/index.php?page={}&tagname=%E5%8A%A8%E6%BC%AB&line=25&tempid=3".format(i)
        main(start_url)
        break
