from bs4 import BeautifulSoup
import urllib

url = "https://www.dbmeinv.com/?pager_offset=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
req = urllib.Request(url, headers)
page = urllib.urlopen(req, timeout=30)
contents = page.read()
print(contents)
