import requests
import re


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWe"
                      "bKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    return res.text


def get_info(html):
    regex = '<dd><a href="(.*?)" title=".*?">(.*?)</a></dd>'
    info_list = re.findall(regex, html, re.S)
    # print(info_list)
    # title_lsit = []
    # url_lsit = []
    x = 1
    for i in info_list:
        # title_lsit.append(i[1])
        # url_lsit.append("http://www.biquke.com/bq/0/990/"+i[0])
        com_url = "http://www.biquke.com/bq/0/990/" + i[0]
        # print(com_url)
        novel_html = get_page(com_url)
        reg = r'<div id="content">(.*?)</div>'
        content = re.findall(reg, novel_html, re.S)[0]
        with open("novel/%s.txt" % i[1], "w", encoding="utf-8") as f:
            f.write(content)
        print("正在下载第%d章" % x)
        x += 1


# try:
html = get_page("http://www.biquke.com/bq/0/990/")
# print(html)
get_info(html)
# print(title_lsit)
# print(url_lsit)
# except Exception as result:
# 	print(result)
