import requests
import hashlib
import random

jsessionId = ""


# 获取占比
def getAsId(asId):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID={}'.format(jsessionId)
    }
    datas = {"asId": asId}
    url = 'http://uims.jlu.edu.cn/ntms/score/course-score-stat.do'
    wb_data = requests.post(url, headers=headers, json=datas).json()
    items = wb_data['items']
    percents = ""
    for item in items:
        percent = int(item['percent'] * 100) / 100
        lable = item['label'][0:2]
        percents = percents + "{}:{} ".format(lable, percent)
    return percents


# 获取成绩
def getScore(jsessionId):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID={}'.format(jsessionId),
        'USER_AGENT': 'Mozila/5.0'
    }
    datas = {"tag": "archiveScore@queryCourseScore", "branch": "latest", "params": {}, "rowLimit": 5}
    url = 'http://uims.jlu.edu.cn/ntms/service/res.do'
    # wb_data = requests.post(url, headers=headers, json=datas)
    # print(wb_data.text)
    wb_data = requests.post(url, headers=headers, json=datas).json()['value']
    print('*' * 20, '{} 你的成绩如下'.format(wb_data[0]['student']['name']), '*' * 20)
    for i in wb_data:
        print(i['teachingTerm']['termName'], i['course']['courName'], i['score'],
              '通过:' + i['isPass'], '\n分值比例是', getAsId(i['asId']))


def get_md5_value(alu, pw):
    src = 'UIMS' + str(alu) + str(pw)
    myMd5 = hashlib.md5()
    myMd5.update(src.encode())
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest


# 登陆
def login(alu, pw):
    jsessionId = '55A{}E240D3D631E458C28C01656G.s12'.format(random.randint(37788, 97788))
    checkUrl = 'http://uims.jlu.edu.cn/ntms/j_spring_security_check'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'alu={};JSESSIONID={}'.format(alu, jsessionId),
        'USER_AGENT': 'Mozila/5.0'
    }
    datas = {
        'j_username': alu,
        'j_password': get_md5_value(alu, pw),
    }
    wb_data = requests.post(url=checkUrl, headers=headers, data=datas)


    # print(wb_data.text)


ids = ["31140320", "31140639"]
pws = ["730422", "730422"]


def start(ids=ids, pws=pws):
    try:
        if (type(ids) != list):
            login(ids, pws)
            getScore(jsessionId)
        else:
            # print("else")
            for id, pw in zip(ids, pws):
                # print(id,pw)
                login(id, pw)
                getScore(jsessionId)
    except:
        print("学校网络出问题")


start()
