from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import sys
import datetime
import random
import requests
import json
import sql
import random
import time

sys.setrecursionlimit(100000000)


# 测试网易云
# params = {'id': 1001, 'initial': 65}
# r = requests.get('http://music.163.com/discover/artist/cat', params=params)
# # 网页解析
# bsobj = BeautifulSoup(r.content, 'html.parser')
#
# UrlAllList = bsobj.find_all("a", attrs={'class': 'nm nm-icn f-thide s-fc0'})
# for list in UrlAllList:
#     # 匹配ID 和歌手名字
#     # print(str(list))
#     Str_idAndName = re.findall(r'<a class="nm nm-icn f-thide s-fc0" href="(.+?)" title="(.+?)">',
#                                str(list), re.S)
#
#     if Str_idAndName:
#         print(Str_idAndName[0][0].replace("/artist?id=", "").strip())
#         print(Str_idAndName[0][1].replace("的音乐", ""))

# artists = sql.get_all_artist()
# print(artists)



# class Album(object):
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Encoding': 'gzip, deflate, sdch',
#         'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
#         'Cache-Control': 'no-cache',
#         'Connection': 'keep-alive',
#         'Cookie': '_ntes_nnid=fdc0e113bec0ba20cf5122867952757f,1481009558059; _ntes_nuid=fdc0e113bec0ba20cf5122867952757f; MUSIC_U=d3d77e6ab688f7f0d9e3b157499573f7b6999fe3cdd3751007634119f6e0ba04c9f350c52f6e7cbf0ea92ca0dcd1435172a4782b5b19e79ede39c620ce8469a8; NETEASE_WDA_UID=118964218#|#1451582239519; vjuids=-108ae1ad6.15996131da7.0.1dd5a8d2881fa; mail_psc_fingerprint=6b8bb42cf43f07a7191585ddafa094fb; UM_distinctid=15adb27164c6e9-095b2d0327c9be-1d3e6850-1fa400-15adb27164d6f2; vjlast=1484281552.1489735458.21; vinfo_n_f_l_n3=137cd7b60cceaa6e.1.2.1484281552324.1486037205195.1489735676316; P_INFO=yllwangyi@163.com|1493976363|0|mail163|00&99|zhj&1493962807&mail_client#zhj&330100#10#0#0|136790&0|yanxuan&mail163|yllwangyi@163.com; __csrf=e3bebe825c52667eb4274846ba9bcb01; JSESSIONID-WYYY=RHoC01ZvhcVs%2F6%5CtrQAtbDmjRzYtR7T0ouZYHGAZQd%2BG2xgtr7BCzN8E3TRqTJAxri7W%2FlXv0JGtp7VtSkg3DuRYmPW8m1HU45D%5C4OVAJmbZSvQ5XtkN7fTjz6xem%2B8s1MY1pNSpIKO7cRM5OBsSE%5CSGa8iRqqtS4Cin2cYRY%2FrlfU3M%3A1500627854080; _iuqxldmzr_=32; __utma=94650624.192912792.1481010208.1497407948.1500626055.87; __utmb=94650624.8.10.1500626055; __utmc=94650624; __utmz=94650624.1497407948.86.28.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
#         'DNT': '1',
#         'Host': 'music.163.com',
#         'Pragma': 'no-cache',
#         'Referer': 'http://music.163.com/',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
#     }
#
#     def save_albums(self, artist_id):
#         params = {'id': artist_id, 'limit': '200'}
#         # 获取歌手个人主页
#         r = requests.get('http://music.163.com/artist/album', headers=self.headers, params=params)
#         # 网页解析
#         bsobj = BeautifulSoup(r.content.decode(), 'html.parser')
#         UrlAllList = bsobj.find_all("a", attrs={'class': 'tit s-fc0'})
#         for list in UrlAllList:
#             Str_idAndName = re.findall(r'<a class="tit s-fc0" href="(.+?)">',
#                                        str(list), re.S)
#             if Str_idAndName:
#                 print(Str_idAndName[0].replace('/album?id=', ''))
#                 sql.insert_album(Str_idAndName[0].replace('/album?id=', ''), artist_id)
#
#
# artists = sql.get_all_artist()
# my_album = Album()
# my_album.save_albums(5210)

class Music(object):
    headers_one = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_ntes_nnid=fdc0e113bec0ba20cf5122867952757f,1481009558059; _ntes_nuid=fdc0e113bec0ba20cf5122867952757f; MUSIC_U=d3d77e6ab688f7f0d9e3b157499573f7b6999fe3cdd3751007634119f6e0ba04c9f350c52f6e7cbf0ea92ca0dcd1435172a4782b5b19e79ede39c620ce8469a8; NETEASE_WDA_UID=118964218#|#1451582239519; vjuids=-108ae1ad6.15996131da7.0.1dd5a8d2881fa; mail_psc_fingerprint=6b8bb42cf43f07a7191585ddafa094fb; UM_distinctid=15adb27164c6e9-095b2d0327c9be-1d3e6850-1fa400-15adb27164d6f2; vjlast=1484281552.1489735458.21; vinfo_n_f_l_n3=137cd7b60cceaa6e.1.2.1484281552324.1486037205195.1489735676316; P_INFO=yllwangyi@163.com|1493976363|0|mail163|00&99|zhj&1493962807&mail_client#zhj&330100#10#0#0|136790&0|yanxuan&mail163|yllwangyi@163.com; __csrf=e3bebe825c52667eb4274846ba9bcb01; JSESSIONID-WYYY=RHoC01ZvhcVs%2F6%5CtrQAtbDmjRzYtR7T0ouZYHGAZQd%2BG2xgtr7BCzN8E3TRqTJAxri7W%2FlXv0JGtp7VtSkg3DuRYmPW8m1HU45D%5C4OVAJmbZSvQ5XtkN7fTjz6xem%2B8s1MY1pNSpIKO7cRM5OBsSE%5CSGa8iRqqtS4Cin2cYRY%2FrlfU3M%3A1500627854080; _iuqxldmzr_=32; __utma=94650624.192912792.1481010208.1497407948.1500626055.87; __utmb=94650624.8.10.1500626055; __utmc=94650624; __utmz=94650624.1497407948.86.28.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        'DNT': '1',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    headers_two = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'ntes_nuid=9877ac876223428c33832062d99d4a5b; vjuids=-437b9ac65.151fb8848bf.0.5354fead; __gads=ID=66d9a6d8e7a992fb:T=1459230004:S=ALNI_MYxXQM7atamO1BHKkhciNFAJgWhDQ; nteslogger_exit_time=1473759925534; usertrack=c+5+hlg/3WTAW3YTDEPtAg==; _ntes_nnid=9877ac876223428c33832062d99d4a5b,1483435296809; mail_psc_fingerprint=1b38b8e2464c0a777b3a02abde52349c; _jzqco=%7C%7C%7C%7C%7C1.1526630400.1495509419678.1495509863080.1495510066682.1495509863080.1495510066682.0.0.0.14.14; NTES_CMT_USER_INFO=85455292%7Cm157****9432%7Chttps%3A%2F%2Fsimg.ws.126.net%2Fe%2Fimg5.cache.netease.com%2Ftie%2Fimages%2Fyun%2Fphoto_default_62.png.39x39.100.jpg%7Cfalse%7CbTE1NzU3MTE5NDMyQDE2My5jb20%3D; P_INFO=m15757119432@163.com|1495509859|2|fa|00&99|zhj&1495264420&tx2#zhj&330100#10#0#0|157432&1|tx2&mail163|15757119432@163.com; __s_=1; __utma=187553192.96281188.1453386194.1482598177.1499481451.8; __utmz=187553192.1499481451.8.1.utmcsr=open.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __oc_uuid=75e56520-e0f7-11e5-9014-8ddcaf948131; _ga=GA1.2.96281188.1453386194; vjlast=1451623991.1500346049.11; vinfo_n_f_l_n3=946bf39d8ad0808f.1.58.1451623991514.1499394874681.1500346123695; JSESSIONID-WYYY=QD8omBaRZzE62BhBpoUtQndVkcFRTNg6lCAVYr2%2Bb%2FgDq7Qd%5CH4%5CmMTw%2B%2FK9eJnRqtmi4m%2BNcttxNFu5xFsEw%2FKw1ViZugDCu2p1390Hqqt9iW%2BWSMAW%5CGRbziIuNMfrD8c377cES0mss%2BBinCYKHfVVN%5CZmaq8pssYGVEQe5IwoCudF%3A1500650000794; _iuqxldmzr_=32; MUSIC_U=c72b3121f48929fbc55c65b12b1179eb39d2df8d807b0caa0447dd8bdad39df6078a7f86c0e87682eb4d8512f971700f31b299d667364ed3; __remember_me=true; __csrf=07c3eaa62ef01e751bea5e15db60e420; __utma=94650624.96281188.1453386194.1499064606.1500648201.6; __utmb=94650624.10.10.1500648201; __utmc=94650624; __utmz=94650624.1500648201.6.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
        'DNT': '1',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }

    headers_there = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': '__utma=94650624.1718354350.1476538933.1500647105.1500650472.274; __utmz=94650624.1497406734.265.38.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ntes_nnid=1bc16447f6b499a02a38e22e9dcfb22a,1476538933972; _ntes_nuid=1bc16447f6b499a02a38e22e9dcfb22a; vjuids=-7d0e359e5.1580a93a016.0.c3fb2bc6ad5368; vjlast=1477646197.1498183124.11; vinfo_n_f_l_n3=62984278e141625d.1.43.1477646196782.1497490116008.1498011422570; __gads=ID=ef1e6703f617a63a:T=1477646198:S=ALNI_MaBFkV4HWVd2INgo8WMOFe_HcGiTA; usertrack=c+5+hVgb6xoSXVH+C+XQAg==; _ga=GA1.2.967553996.1478582563; ntes_renjian=%2C%E6%9D%80%E9%A9%AC%E7%89%B9%E7%B3%BB%E5%88%97%7C03%7Chttp%3A%2F%2Frenjian.163.com%2F16%2F1108%2F17%2FC5C88GNF000181RK.html%2C%E5%9C%B0%E5%B9%B3%E7%BA%BF-%E6%9D%80%E9%A9%AC%E7%89%B9%E5%B0%91%E5%B9%B4%7C%7Chttp%3A%2F%2Frenjian.163.com%2F17%2F0308%2F18%2FCF1A8Q8E000181RK.html%2C%E5%B7%A5%E5%8E%82%E7%94%B7%E5%AD%A9%7C05%7Chttp%3A%2F%2Frenjian.163.com%2F17%2F0406%2F17%2FCHBT672U000181RV.html; NTES_REPLY_NICKNAME=yllwangyi%40163.com%7Cyllwangyi%7C%7C%7C%7C%7C1%7C-1; mail_psc_fingerprint=00da2a9548949d0c9ec3d0141a484010; UM_distinctid=15ac5318dbb2c4-02bb1a92653f2f-495368-1fa400-15ac5318dbd18a; JSESSIONID-WYYY=xRIUdy%2B%2FsfPtyGQQBagcj%5C3ewnQS%5CH3xicRV2lu6hCl3Qfch8ZWtd3Pi2s9651R142efwxbOn3Nier1kk46PkGDyi7RNTE8oTh%5CIu9ZxYA%5C8CQTqKEEPe9D%5CABeYXzHvvFfzxMDEgRYKUBURiNYGqsEmGJa%5CF6yuuUJKgS2Q4jjydvkc%3A1500650953630; _iuqxldmzr_=32; NTES_CMT_USER_INFO=101222061%7Cyllwangyi%7Chttps%3A%2F%2Fsimg.ws.126.net%2Fe%2Fimg5.cache.netease.com%2Ftie%2Fimages%2Fyun%2Fphoto_default_62.png.39x39.100.jpg%7Cfalse%7CeWxsd2FuZ3lpQDE2My5jb20%3D; __csrf=d427573b550bf5a8c33c67e33d261dbb; NTES_SESS=nuIBKKG2xAKi3CL53xkgXZ5o6PWBeO9VACDOrj09ZCcowsISwc4gjprRnCENoGcjSbBP6gKE5hWbQ52ryyu4KdORcjTu8Nno_nZrf5iEvftdnruUTRvDFmkX7ccGMI3lcOtm.HzTVmTVxrCVjqujgUhi_Ltix5UHGVTHmM4GOh3sirKZ3pyaTiCGn_hhgZP5Q; S_INFO=1499935832|0|2&70##|yllwangyi; P_INFO=yllwangyi@163.com|1499935832|0|mail163|00&99|zhj&1499874019&mail_client#zhj&330100#10#0#0|136790&0|cloudmusic&mail163|yllwangyi@163.com; MUSIC_EMAIL_U=d3d77e6ab688f7f0d9e3b157499573f76afe79cdc30c3b1d01d1de1dbb2f7ed083af2db9e7e0e324afe1efab4d25165959f738c734f0149ade39c620ce8469a8; playliststatus=visible; __utmc=94650624; __s_=1; __utmb=94650624.12.10.1500650472; __remember_me=true; MUSIC_U=9de0b492647e4661059641066c9fbba88c2a4906cea5aa10a78f19fb8b56c315cce0da4f59505407433b1b8af96a6ac687b61297f74eee949b62e231d78ba22d719111a94fb470b4',
    }

    def save_music(self, album_id):
        params = {'id': album_id}
        # 获取专辑对应的页面
        # 这里做一个cookie切换
        num = random.randint(0, 2)
        if num == 0:
            r = requests.get('http://music.163.com/album', headers=self.headers_one, params=params)
        elif num == 1:
            r = requests.get('http://music.163.com/album', headers=self.headers_two, params=params)
        else:
            r = requests.get('http://music.163.com/album', headers=self.headers_there, params=params)
        # 网页解析
        soup = BeautifulSoup(r.content.decode(), 'html.parser')

        body = soup.body
        # 取到ul class 然后再找li
        musics = body.find('ul', attrs={'class': 'f-hide'}).find_all('li')  # 获取专辑的所有音乐
        for music in musics:
            music = music.find('a')
            music_id = music['href'].replace('/song?id=', '')
            music_name = music.getText()
            print(num)
            print(music_name)

            sql.insert_music(music_id, music_name, album_id)


if __name__ == '__main__':
    albums = sql.get_all_album()
    print(albums)
    my_music = Music()
for i in albums:
    try:
        my_music.save_music(i['ALBUM_ID'])
        # print(i)
    except Exception as e:
        # 打印错误日志
        print(str(i) + ': ' + str(e))
        time.sleep(5)
