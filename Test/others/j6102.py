import requests
import re


def get_res(url):
    r = requests.get(url)
    r.encoding = "utf-8"
    r.close()
    return r


def get_gif(html):
    regex = r'img.*?src="(.*?)"'
    url_list = re.findall(regex, html)
    global x
    for gif_url in url_list:
        url = "http://qq.yh31.com/" + gif_url
        text = get_res(url).content
        with open("./imags/2/%d.gif" % x, "wb") as f:
            f.write(text)
            x += 1


if __name__ == '__main__':
    x = 1
    url = ["http://qq.yh31.com/zjbq/2920180.html", "http://qq.yh31.com/zjbq/2920180_2.html"]
    for i in url:
        html = get_res(i).text
        get_gif(html=html)

