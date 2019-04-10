import requests
from bs4 import BeautifulSoup


try:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleW"
                             "ebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    r = requests.get("http://www.meizitu.com/", headers=headers, timeout=30)
    print(r.status_code)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    img_tag = soup.find("img")
    img_url = img_tag.get("src")
    # print(img_url)
    rsp = requests.get(img_url, headers, timeout=30)
    file = open("./imags/1.jpg", "wb")
    file.write(rsp.content)
    file.close()
    rsp.close()


except Exception as result:
    print(result)

