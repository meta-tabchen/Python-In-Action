import requests

postUrl = 'http://uims.jlu.edu.cn/ntms/eduEvaluate/eval-with-answer.do'


def postItem(id, jsessionId):
    print(id, jsessionId)
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


def getIds(jsessionId):
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


# postItem(4105534)
# getIds('A4F3E472B537AE3D55EE7BAD9039163E.s32')

# wb_data = requests.get('http://uims.jlu.edu.cn/ntms/userLogin.jsp?reason=logout')
# print(wb_data.headers)

# postItem(3841721, '44408DE324D084F618125696A2566CC.s34')
