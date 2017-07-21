from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import sys
import datetime
import random
import requests
import json

sys.setrecursionlimit(100000000)


# 帖子主题详情
def DeailPost(url, page):
    html = urlopen("https://tieba.baidu.com%s&pn=%s" % (url, page))
    bsobj = BeautifulSoup(html, "html.parser")
    # 提取内容
    DeatilList = re.findall(
        r'<div class="d_post_content j_d_post_content " id="post_content_\d+">            (.+?)</div>',
        str(bsobj), re.S)
    for Deail in DeatilList:
        # 正则 替换表情 <>
        moduel = re.compile('<.*>')
        info = re.sub(moduel, '', Deail.replace('<br/>', ','))
        if len(info) > 10:
            print(info)
            num = random.randint(0, 10)
            with open("Tieba%d.txt" % num, 'a') as obj:
                obj.write(info + '\n')


# 查看帖子有多少页
def PageDeatil(url):
    html = urlopen("https://tieba.baidu.com%s&pn=1" % url)
    bsobj = BeautifulSoup(html, "html.parser")
    # 提取出页数
    PageDeatilList = re.findall(r'共<span class="red">(.+?)</span>页</li>', str(bsobj), re.S)
    if PageDeatilList:
        for page in range(1, int(PageDeatilList[0]) + 1):
            DeailPost(url, page)


# PageDeatil('/p/4769918116?fr=good')


# 帖子列表

def PostList(page):
    html = urlopen("https://tieba.baidu.com/f/good?kw=%E6%89%93%E6%B2%B9%E8%AF%97&ie=utf-8&cid=0&pn=" + page)
    bsobj = BeautifulSoup(html, "html.parser")
    UrlAllList = bsobj.find_all("a", )
    for url in UrlAllList:
        # print(str(url)+"\n")
        # 开始匹配帖子URL
        url_PostList = re.findall(r'<a class="j_th_tit" href="(.+?)" target="_blank" title="', str(url), re.S)
        if url_PostList:
            PageDeatil(url_PostList[0])


for page in range(0, 250, 50):
    PostList(str(page))
