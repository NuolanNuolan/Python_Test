import requests, json

# 执行api调用并储存响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.headers)
