"""
根据上一步获取的歌手的 ID 来用于获取所有的专辑 ID
"""
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
import time


class Album(object):
    headers = {
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

    def save_albums(self, artist_id):
        params = {'id': artist_id, 'limit': '200'}
        # 获取歌手个人主页
        r = requests.get('http://music.163.com/artist/album', headers=self.headers, params=params)
        # 网页解析
        bsobj = BeautifulSoup(r.content.decode(), 'html.parser')
        UrlAllList = bsobj.find_all("a", attrs={'class': 'tit s-fc0'})
        for list in UrlAllList:
            Str_idAndName = re.findall(r'<a class="tit s-fc0" href="(.+?)">',
                                       str(list), re.S)
            if Str_idAndName:
                print(Str_idAndName[0].replace('/album?id=', ''))
                sql.insert_album(Str_idAndName[0].replace('/album?id=', ''), artist_id)


if __name__ == '__main__':
    artists = sql.get_all_artist()
    my_album = Album()
    for i in artists:
        try:
            my_album.save_albums(i['ARTIST_ID'])
            # print(i)
        except Exception as e:
            # 打印错误日志
            print(str(i) + ': ' + str(e))
            time.sleep(5)
