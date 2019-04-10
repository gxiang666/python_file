import json
import requests
from requests.exceptions import RequestException
import re
import pymysql
import sys

# python3抓取房天下资讯存入mysql
url = str(sys.argv[1])  # 接收php传的参数
agent_id = str(sys.argv[2])


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWe'
                      'bKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    reg = re.compile('<!--(.*?)-->')
    content = reg.sub('', html)
    pattern = re.compile(
        '<div.*?infoBox-item.*?<h3.*?href="(.*?)".*?>(.*?)</a></h3>.*?comment.*?</span>.*?<span>(.*?)</span>.*?</div>',
        re.S)
    items = re.findall(pattern, content)
    for item in items:
        yield {
            'agent_id': agent_id,
            'purl': item[0],
            'title': item[1],
            'source': '房天下',
            'ftime': item[2]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    db = pymysql.connect("127.0.0.1", "root", "123456", "test")
    cursor = db.cursor()

    html = get_one_page(url)
    L = []
    for item in parse_one_page(html):
        data = item
        L.append(tuple(data.values()))  # list添加新元素

    sql = "INSERT INTO wzl_newscollect(agent_id, purl, title, source, ftime) VALUES (%s,%s,%s,%s,%s)"
    try:
        cursor.executemany(sql, L)
        print('success')
        db.commit()
    except:
        print('fail')
        db.rollback()
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
