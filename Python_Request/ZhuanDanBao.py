from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import sys
sys.setrecursionlimit(100000000)





# 定义店铺信息字典
ShopDeailList = {}
ShopDeatilArr = []


# 获取店铺详细信息
def getDeatil(url):
    html = urlopen("http://www.zhuandan.com%s" % url)
    bsobj = BeautifulSoup(html, "html.parser")
    PopoleList = re.findall(r'<th class="w100">联 系 人：</th>\n<td>(.+?)</td>', str(bsobj), re.S)
    PhoneList = re.findall(r'<th class="w100">联系电话：</th>\n<td><img src="(.+?)"/>  <img src="(.+?)"/></td>', str(bsobj),
                           re.S)
    EmailList = re.findall(r'<th class="w100">电子邮箱：</th>\n<td>(.+?)</td>', str(bsobj), re.S)
    QQList = re.findall(r'<th class="w100">QQ号码：</th>\n<td>(.+?)</td>', str(bsobj), re.S)
    AddList = re.findall(r'<th class="w100">店铺地址：</th>\n<td>(.+?)</td>', str(bsobj), re.S)
    ShopDeailList["姓名"] = PopoleList[0]
    PhoneArr = []
    for phone in PhoneList:
        PhoneArr.append(phone)
    ShopDeailList["电话"] = PhoneArr
    ShopDeailList["邮箱"] = EmailList[0]
    ShopDeailList["QQ"] = QQList[0]
    ShopDeailList["地址"] = AddList[0]
    # ShopDeatilArr.append(ShopDeailList)
    # print(ShopDeailList)
    print(str(ShopDeailList))
    with open("ZhuanDanBao.txt", 'a') as obj:
        obj.write(str(ShopDeailList)+'\n')


# 定义店铺URL数组
ShopList = []


# 抓取店铺URL
def getUrlList(num):
    html = urlopen("http://www.zhuandan.com/store?&p=%s" % num)
    bsobj = BeautifulSoup(html, "html.parser")
    UrlList = bsobj.find_all("a")
    for url in UrlList:
        if "进入店铺" in url:
            numlist = re.findall(r'<a class="btn btn-info btn-xs" href="(.+?)" target="_blank">进入店铺</a>', str(url),
                                 re.S)
            getDeatil(numlist[0])
            ShopList.append(numlist[0])

    num += 1
    getUrlList(num)


getUrlList(1)