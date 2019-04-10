import re
import requests


class Spider:
    def __init__(self):
        self.session = requests.Session()

    def download(self, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK"
                                 "it/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"}
        response = self.session.get(url, headers=headers)
        response.close()
        return response

    def get_img_item_url(self, url):

        response = self.download(url).text
        regex = r'<div id="picture"><p><a href="(.*?)" title=".*?".*?><img src=".*?" style=".*?" /></a></p></div>'
        img_item_url = re.findall(regex, response, re.S)
        return img_item_url

    def main(self, start_url):
        img_item_url = self.get_img_item_url(start_url)
        print(img_item_url)


spider = Spider()
spider.main("http://www.meizitu.com/")
