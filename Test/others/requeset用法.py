import requests
r = requests.get("https://www.bilibili.com/video/av9784617?p=5")
print(r.status_code)
r.encoding = "utf-8"
print(r.content)
