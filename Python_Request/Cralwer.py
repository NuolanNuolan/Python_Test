from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.error import HTTPError
import re
from twitter import Twitter
import sys
import datetime
import random
import requests
import json


sys.setrecursionlimit(100000000)

# 获取title
# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except:
#         return None
#     try:
#         bsobj = BeautifulSoup(html, "html.parser")
#         title = bsobj.h1
#     except AttributeError as e:
#         return None
#     return title
#
#
# title = getTitle("http://www.pythonscraping.com/pages/page1.html")
# if title == None:
#     print('Error')
# else:
#     print(title)

# find方法
# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsobj = BeautifulSoup(html, "html.parser")
# # nameList = bsobj.find_all("span",{"class": "red"})
# nameList = bsobj.find_all(text="the prince")
# print(nameList)

# 导航树
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsobj = BeautifulSoup(html, "html.parser")
# 子标签
# for child in bsobj.find("table",{"id":"giftList"}).children:
# print(child)

# 兄弟标签
# for sibling in bsobj.find("table", {"id": "gifList"}).tr.next_siblings:
#     print(sibling)
# 同级标签 上一个标签
# print(bsobj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
# 正则表达式
# images = bsobj.find_all("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
#
# print(images)
# 提取网页信息
# str = '<span class="link_title"><a href="/u013074465/article/details/44280335">\n《unix网络编程（卷1）》源代码的使用方法\n</a></span>'

# allfinds = re.findall(r'<span class="link_title"><a href="/u013074465/article/details/........">\n(.+?)\n</a></span>',
# str, re.S)
# print(allfinds[0].strip())

# html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
# bsobj = BeautifulSoup(html, "html.parser")
# for link in bsobj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$")):
#     print(link)

# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen("https://en.wikipedia.org"+pageUrl)
#
#     bsObj = BeautifulSoup(html,"html.parser")
#     try:
#         print(bsObj.h1.get_text())
#         print(bsObj.find(id="mw-content-text").findAll("p")[0])
#         print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
#     except AttributeError:
#         print("页面缺少一些属性!不过不用担心!")
#     for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 # 我们遇到了新页面
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
# getLinks("")

# html = requests.get("http://freegeoip.net/json/50.78.253.58")
#
# print(html.json().get('metro_code'))

# jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
#
# jsonObj = json.loads(jsonString)
# print(jsonObj)


# random.seed(datetime.datetime.now())
#
# def getLinks(articleUrl):
#     html = urlopen("https://en.wikipedia.org" + articleUrl)
#     bsobj = BeautifulSoup(html, "html.parser")
#     return bsobj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
#
#
# def getHistoryIPs(pageUrl):
#     # 编辑历史页面URL链接格式是:
#     pageUrl = pageUrl.replace("/wiki/", "")
#     historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
#     # print(historyUrl)
#     html = urlopen(historyUrl)
#     bsobj = BeautifulSoup(html, "html.parser")
#     ipAddress = bsobj.find_all("a", {"class": "mw-anonuserlink"})
#     addressList = set()
#     for ipAdd in ipAddress:
#         addressList.add(ipAdd.get_text())
#     return addressList
#
#
# links = getLinks("/wiki/Python_(programming_language)")
#
# while (len(links) > 0):
#     for link in links:
#         print("-------------------")
#         historyIPs = getHistoryIPs(link.attrs["href"])
#         for historyIP in historyIPs:
#             print(historyIP)
#     newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
#     links = getLinks(newLink)

url = 'http://10.176.1.254/web/device/login?lang=1'
html = urlopen(url)
bsobj = BeautifulSoup(html, "html.parser")
print(bsobj)
