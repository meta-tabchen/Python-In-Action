import requests
import re
import time
import datetime

url = 'https://h5.qzone.qq.com/mqzone/index'

# 请求头
cookies = 'tvfe_boss_uuid=ebbab6cc018aab93; mobileUV=1_15ae6230008_5b30a; pgv_pvid=3613555820; pgv_pvi=2122076160; RK=7TmTXQk+T1; _qpsvr_localtk=0.09430412013708178; pgv_si=s8307500032; pgv_info=ssid=s2328249485; ptui_loginuin=2808581543; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; qq_photo_key=82b492af14bc23dae3e421c771c1ae7f; zzpaneluin=; zzpanelkey=; ptcz=c163065bea89abb519e805ecc12a80e8f767ddbd2a6c1052f93233f75583e31b; ptisp=cm; pt2gguin=o2808581543; uin=o2808581543; skey=@z0q28zTIA; p_uin=o2808581543; p_skey=FBD6AO70dn9cIMFNkPtPa9rLE2awh2KQtVHQZnxhAm0_; pt4_token=Rh9UAIJx1UMgbnjAAd*sItZtQYULgM-ucbAhzq9zInw_; qzspeedup=sdch; Loading=Yes; cpu_performance_v8=9; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; qzmusicplayer=qzone_player_2781792072_1496122239504; rv2=80D00FB12794FC9EBA9CF3F46A383FE6C8A264B58C38062316; property20=78753EFF14E6015F4DC3F91AB9F0C1ECB3928708B8E837203021D69423708ADCA44B4D62354527CD; QZ_FE_WEBP_SUPPORT=1'
headers = {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'X-Requested-With': 'XMLHttpRequest',
    # 'Referer': 'https://h5.qzone.qq.com/mqzone/index',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie': cookies,
    # 'origin': 'https://h5.qzone.qq.com',
    # 'upgrade-insecure-requests': '1'
}


def like(orglikekey, curlikekey):
    url = 'https://h5.qzone.qq.com/proxy/domain/w.qzone.qq.com/cgi-bin/likes/internal_dolike_app?&g_tk=1187263162'

    datas = {'opuin': '2808581543',
             'unikey': orglikekey,
             'curkey': curlikekey,
             'format': 'purejson'}

    like_data = requests.post(url, headers=headers, data=datas)

    # print(like_data.text)


def unLike(orglikekey, curlikekey):
    url = 'https://h5.qzone.qq.com/proxy/domain/w.qzone.qq.com/cgi-bin/likes/internal_unlike_app?&g_tk=1187263162'
    datas = {'opuin': '2808581543',
             'unikey': orglikekey,
             'curkey': curlikekey,
             'format': 'purejson'}
    unLike_data = requests.post(url, headers=headers, data=datas)
    # print(unLike_data.text)


def likeIndex():
    url = 'https://h5.qzone.qq.com/mqzone/index'
    wb_data = requests.post(url, headers=headers)
    keys = list(set(re.findall('http://user.qzone.qq.com/[\S]{6,14}/[\s\S]*?"', wb_data.text)))
    for key in keys:
        time.sleep(1)
        # unLike(key.split('"'))
        like(key.split('"'))


def changeTimeFormat(timestamps):
    return [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)) for x in timestamps]

number=0
def getKeysFromJson(bastime):
    global number

    url = 'https://h5.qzone.qq.com/webapp/json/mqzone_feeds/getActiveFeeds?g_tk=1187263162'
    # bastime=1496106742
    temp = 'back_server_info=basetime%3D{}'.format(bastime)

    datas = {'res_type': '0',
             # '&res_attach':temp,
             # 'refresh_type': '2',
             # 'format': 'json',
             'attach_info': temp
             }
    wb_data = requests.post(url, headers=headers, data=datas).json()
    items = wb_data['data']['vFeeds']
    names = [name['userinfo']['user']['nickname'] for name in items]
    orglikekeys = [item['comm']['orglikekey'] for item in items]
    curlikekeys = [item['comm']['curlikekey'] for item in items]

    timestamps = [x['userinfo']['user']['timestamp'] for x in items]
    basetime = timestamps[-1]
    ###################################
    # 这是递归调用来实现所有的点赞
    timestamps = changeTimeFormat(timestamps)
    for orglikekey, name, timestamp, curlikekey in zip(orglikekeys, names, timestamps, curlikekeys):
        number = number + 1
        time.sleep(1)
        like(orglikekey, curlikekey)
        # unLike(orglikekey, curlikekey)
        print(orglikekey.strip(), name.strip(), timestamp, curlikekey)
    time.sleep(2)
    print('目前已经完成的总数',number)
    getKeysFromJson(basetime)  # 用当前的时间当入口来调用



getKeysFromJson(int(time.clock()))
# print(int(time.time()))
# print(int(time.time()))
# times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamps))
# print(times)
# like('https://sojump.com/m/14520887.aspx?from=groupmessage')
# unLike('https://sojump.com/m/14520887.aspx?from=groupmessage')
