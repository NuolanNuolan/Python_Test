"""
根据歌曲 ID 获得所有的歌曲所对应的评论信息
"""

import requests
import sql
import time
import threading
import pymysql.cursors


class Comments(object):
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

    params = {
        'csrf_token': ''
    }

    data = {
        'params': 'Ak2s0LoP1GRJYqE3XxJUZVYK9uPEXSTttmAS+8uVLnYRoUt/Xgqdrt/13nr6OYhi75QSTlQ9FcZaWElIwE+oz9qXAu87t2DHj6Auu+2yBJDr+arG+irBbjIvKJGfjgBac+kSm2ePwf4rfuHSKVgQu1cYMdqFVnB+ojBsWopHcexbvLylDIMPulPljAWK6MR8',
        'encSecKey': '8c85d1b6f53bfebaf5258d171f3526c06980cbcaf490d759eac82145ee27198297c152dd95e7ea0f08cfb7281588cdab305946e01b9d84f0b49700f9c2eb6eeced8624b16ce378bccd24341b1b5ad3d84ebd707dbbd18a4f01c2a007cd47de32f28ca395c9715afa134ed9ee321caa7f28ec82b94307d75144f6b5b134a9ce1a'
    }

    proxies = {'http': 'http://127.0.0.1:10800'}

    def get_comments(self, music_id, flag):
        self.headers['Referer'] = 'http://music.163.com/playlist?id=' + str(music_id)
        if flag:
            r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(music_id),
                              headers=self.headers, params=self.params, data=self.data, proxies=self.proxies)
        else:
            r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(music_id),
                              headers=self.headers, params=self.params, data=self.data)
        return r.json()


if __name__ == '__main__':
    my_comment = Comments()


    def save_comments(musics, flag, connection0):
        for i in musics:
            my_music_id = i['MUSIC_ID']
            try:
                comments = my_comment.get_comments(my_music_id, flag)
                if comments['total'] > 0:
                    print(comments)
                    # sql.insert_comments(my_music_id, comments['total'], str(comments), connection0)
            except Exception as e:
                # 打印错误日志
                print(my_music_id)
                print(e)
                time.sleep(5)


    music_before = sql.get_before_music()
    music_after = sql.get_after_music()

    # pymysql 链接不是线程安全的
    connection1 = pymysql.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  db='Eason_Test',
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)

    connection2 = pymysql.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  db='Eason_Test',
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)

    t1 = threading.Thread(target=save_comments, args=(music_before, True, connection1))
    t2 = threading.Thread(target=save_comments, args=(music_after, False, connection2))
    t1.start()
    t2.start()
