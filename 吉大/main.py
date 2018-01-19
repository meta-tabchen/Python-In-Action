import time
import requests
import hashlib

jsessionId = '55A37788E240D3D931E458C27C01656D.s12'


# 获取成绩
def getScore(jsessionId):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID={}'.format(jsessionId)
    }
    datas = {"tag": "archiveScore@queryCourseScore", "branch": "latest", "params": {}, "rowLimit": 150}
    url = 'http://uims.jlu.edu.cn/ntms/service/res.do'
    # wb_data = requests.post(url, headers=headers, json=datas)
    # print(wb_data.text)
    wb_data = requests.post(url, headers=headers, json=datas).json()['value']
    print('{}\n你的成绩如下'.format(wb_data[0]['student']['name']))
    for i in wb_data:
        print(i['teachingTerm']['termName'], i['course']['courName'], i['score'],
              '通过：' + i['isPass'])


def postItem(id, jsessionId):
    postUrl = 'http://uims.jlu.edu.cn/ntms/eduEvaluate/eval-with-answer.do'
    # print(id, jsessionId)
    headers = {
        'Content-Type': 'application/json',
        'Referer': 'http://uims.jlu.edu.cn/ntms/page/eval/eval_detail_100.html?eitem={}'.format(str(id)),
        'Cookie': 'JSESSIONID={}'.format(jsessionId)
    }

    datas = {"evalItemId": id,
             "answers": {"prob11": "A", "prob12": "A", "prob13": "D", "prob14": "A", "prob15": "A", "prob21": "A",
                         "prob22": "A", "prob23": "A", "prob31": "A", "prob32": "A", "prob41": "A", "prob42": "A",
                         "prob43": "A", "prob51": "A", "prob52": "A", "sat6": "A", "mulsel71": "L", "advice8": ""}}
    print('getInfo')

    wb_data = requests.post(postUrl, headers=headers, json=datas)
    # print(wb_data.text)


# 评教
def eduEvaluate(jsessionId):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID={}'.format(jsessionId)
    }
    datas = {"tag": "student@evalItem", "branch": "self", "params": {"blank": "Y"}}
    url = 'http://uims.jlu.edu.cn/ntms/service/res.do'
    wb_data = requests.post(url, headers=headers, json=datas).json()['value']
    print('正在评教中---------')
    for i in wb_data:
        print(i['evalItemId'])
        postItem(i['evalItemId'], jsessionId)


# 加密密码
def get_md5_value(alu, pw):
    src = 'UIMS' + str(alu) + str(pw)
    myMd5 = hashlib.md5()
    myMd5.update(src.encode())
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest


# 登陆
def login(alu, pw):
    checkUrl = 'http://uims.jlu.edu.cn/ntms/j_spring_security_check'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'alu={};JSESSIONID={}'.format(alu, jsessionId)
    }
    datas = {
        'j_username': alu,
        'j_password': get_md5_value(alu, pw),
    }
    wb_data = requests.post(url=checkUrl, headers=headers, data=datas)
    # print(wb_data.raw)


def start():
    print('*' * 10, '欢迎使用查询系统', '*' * 10)
    event = input('请输入选项:\n1.查询所有的成绩 2.一键评教:\n')
    try:
        event = int(event)
        if event == 1:
            print('正在执行: 查询所有成绩')
        else:
            print('正在执行: 一键评教')

        id = input('学号:\n')
        pw = input('密码:\n')
        login(id, pw)
        # login(31140639, 730422)
        if event == 1:
            getScore(jsessionId)
        else:
            eduEvaluate(jsessionId)
        print('*' * 10, '执行完毕', '*' * 10)
        over = input('\n再次执行输入：start 退出输入：exit :\n')
        if over == 'exit':
            print('再见！欢迎下次使用')
        else:
            start()

    except:
        print('你可能输错了！！')
    # start()

