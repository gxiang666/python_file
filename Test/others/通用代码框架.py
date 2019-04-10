import requests


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    # except:
    #     return  "产生异常"
    except Exception as result:
        return result


if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(get_html_text(url))
