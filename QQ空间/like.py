import requests
import re
import time
url = 'https://h5.qzone.qq.com/mqzone/index'

# 请求头
cookies ='tvfe_boss_uuid=ebbab6cc018aab93; mobileUV=1_15ae6230008_5b30a; pgv_pvid=3613555820; pgv_pvi=2122076160; RK=7TmTXQk+T1; _qpsvr_localtk=0.09430412013708178; pgv_si=s8307500032; pgv_info=ssid=s2328249485; ptui_loginuin=2808581543; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; qq_photo_key=82b492af14bc23dae3e421c771c1ae7f; rv2=80786F203B13266E6E0631C7C7062A95DFCB86BE1992598DE3; property20=7CBC7EE1ED4E03B830AA4CB42BA1CE2A4643F77DDA99B44FA7FD2C0E8C13B309384FFAFBA8FE8A75; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; qzmusicplayer=qzone_player_992613160_1496108888264; zzpaneluin=; zzpanelkey=; ptcz=c163065bea89abb519e805ecc12a80e8f767ddbd2a6c1052f93233f75583e31b; cpu_performance_v8=27; ptisp=cm; ptmbsig=d4ba8f18cc3b0cc80de7dd50aec8c2c7ec877943eae7171d817cfea7da3e86476dfaff8df0fd4900; pt2gguin=o2808581543; uin=o2808581543; skey=@z0q28zTIA; p_uin=o2808581543; p_skey=TvKvIvH9UVTnxBU6j-5eQ2L-I99s7uTZo0xmtGX2mqs_; pt4_token=Wg3zs1YROEXjXMiMWPQafdLdoQZMkvDcIlsvF7G5F1I_; Loading=Yes; qzspeedup=sdch; qz_screen=375x667; 2808581543_todaycount=0; 2808581543_totalcount=27668; QZ_FE_WEBP_SUPPORT=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie': cookies}


def like(unikey):
    url = 'https://h5.qzone.qq.com/proxy/domain/w.qzone.qq.com/cgi-bin/likes/internal_dolike_app?&g_tk=1187263162'

    datas = {'opuin': '2808581543',
             'unikey': unikey,
             'format': 'purejson'}

    like_data = requests.post(url, headers=headers, data=datas)

    print(like_data.text)


def unLike(unikey):
    url = 'https://h5.qzone.qq.com/proxy/domain/w.qzone.qq.com/cgi-bin/likes/internal_unlike_app?&g_tk=1187263162'
    datas = {'opuin': '2808581543',
             'unikey': unikey,
             'format': 'purejson'}
    unLike_data = requests.post(url, headers=headers, data=datas)
    print(unLike_data.text)


def getKeys(loadCount):
    datas = {'loadcount': loadCount,
             }

    url = 'https://h5.qzone.qq.com/webapp/json/mqzone_feeds/getActiveFeeds?g_tk=1187263162'

    wb_data = requests.post(url, headers=headers, data=datas)
    print(wb_data.raw)
    keys = list(set(re.findall('http://user.qzone.qq.com/[\S]{6,14}/[\s\S]*?"', wb_data.text)))
    for key in keys:
        time.sleep(3)
        like(key.split('"'))


def goLike(start,end):
    for i in range(start, end):
        getKeys(i)


# like('http://user.qzone.qq.com/992613160/batchphoto/V13kuQ394A8YRu/1496102407491')
# unLike()
getKeys(1)
# goLike(1,3)
