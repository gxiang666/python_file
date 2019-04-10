# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup

url = "https://www.dbmeinv.com/?pager_offset=2"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKi"
                         "t/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

req = urllib2.Request(url, headers=headers)
page = urllib2.urlopen(req, timeout=30)
contents = page.read()
soup = BeautifulSoup(contents, "html.parser")
x = 20
my_girl = soup.find_all("img")
for girl in my_girl:
    link = girl.get("src")
    urllib.urlretrieve(link, "images\%s.jpg" % x)
    x += 1

