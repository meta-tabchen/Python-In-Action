import requests


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
    print(wb_data.text)

#评教
def eduEvaluate(jsessionId):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID={}'.format(jsessionId)
    }
    datas = {"tag": "student@evalItem", "branch": "self", "params": {"blank": "Y"}}
    url = 'http://uims.jlu.edu.cn/ntms/service/res.do'
    wb_data = requests.post(url, headers=headers, json=datas).json()['value']
    for i in wb_data:
        print(i['evalItemId'])
        postItem(i['evalItemId'], jsessionId)
