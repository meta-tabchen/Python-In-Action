import requests
import time
import random


def get_header():
    Header = {"Content-Type": "application/json",
              "Cookie": "JSESSIONID=7D1D1685FE9F712D59B01EFD61CD100E.s44"}
    return Header


def execte_url(url, data):
    wb_data = requests.get(url, headers=get_header(), json=data)
    return wb_data.json()


# 获取虚假日期
def getFakeDate():
    years = [2017, 2016, 2015, 2014]
    year = random.choices(years)[0]
    low = 1
    high = 13
    if (year == 2014):
        low = 10
    if (year == 2017):
        high = 10
    mouth = random.randint(low, high)
    data = random.randint(1, 20)
    dateStart = "{}-{}-{}".format(year, mouth, data)
    dateStop = "{}-{}-{}".format(year, mouth, data + random.randint(1, 5))
    # dateStart = "2020-11-1"
    # dateStop = "2017-11-1"
    return dateStart, dateStop


def add_stu_social_prac():
    dateStart, dateStop = getFakeDate()
    dateStart = "{}T00:00:00+08:00".format(dateStart)
    dateStop = "{}T00:00:00+08:00".format(dateStop)
    print(dateStart, dateStop)
    url = 'add-stu-social-prac'
    data = {
        "practice": {"name": "社会实习", "dateStart": dateStart, "dateStop": dateStop,
                     "organUnit": "华航大学生", "organizer": "组织部", "staffId": "", "isAward": "N"},
        "member": [{"person": {"personId": 241753}, "role": "0", "rank": "1"}]}


def submit(achievementId):
    url = "http://ptms.jlu.edu.cn/ptms/pAction/extraTrain/submit-achievement.do"
    data = {"achievementId": achievementId}
    return execte_url(url, data)


def add_campus_cul(name, organUnit="华航大学生志愿团", organizer="组织部", address="逸夫楼"):
    dateStart, dateStop = getFakeDate()
    dateStart = "{}T00:00:00+08:00".format(dateStart)
    dateStop = "{}T00:00:00+08:00".format(dateStop)
    print(dateStart, dateStop)
    url = 'http://ptms.jlu.edu.cn/ptms/pAction/extraTrain/add-campus-cul.do'
    data = {"practice": {"name": name, "organUnit": organUnit, "organizer": organizer,
                         "dateStart": dateStart, "dateStop": dateStop,
                         "address": address, "staffId": ""},
            "member": [{"person": {"personId": 241753}, "role": "0", "rank": "1"}]}
    return execte_url(url, data)


def delete_activity(practiceId):
    url = 'http://ptms.jlu.edu.cn/ptms/pAction/extraTrain/delete-other-pro-activity.do'
    data = {"practiceId": practiceId}
    return execte_url(url, data)


activities = {"社会实践": 'socialPrac', "等级考试": "gradeExam", "校园文化": "stuCampusCul", "专业拓展": "proExpansion",
              "交流访学": "stuInterviewMgr"}


def get_all_activity():
    url = 'http://ptms.jlu.edu.cn/ptms/service/res.do'

    data = {"tag": "search@stuCampusCul", "branch": "stu",
            "params": {"name": "", "state": "", "personId": "", "mine": 1}}
    return execte_url(url, data)


def get_all_id():
    data = get_all_activity()
    ids = []
    values = data['value']
    for value in values:
        id = value['practiceId']
        ids.append(id)
    return ids


def deleteAllInput():
    ids = get_all_id()
    print(ids)
    for id in ids:
        print(delete_activity(id))


names = [""]


def temp():
    import os
    import os.path

    # this folder is custom
    rootdir = "D:/360Downloads/testFile1"
    for parent, dirnames, filenames in os.walk(rootdir):
        # case 1:
        for dirname in dirnames:
            print("parent folder is:" + parent)
            print("dirname is:" + dirname)
            # case 2
        for filename in filenames:
            print("parent folder is:" + parent)
            print("filename with full path:" + os.path.join(parent, filename))
    print(names)

# names = readFileName()
# for name in names:
#     print(add_campus_cul(name))

def readFileName():
    import os
    import os.path
    names = []
    rootDir = 'E:\毕业\读后感'
    for parent, dirnames, filenames in os.walk(rootDir):
        for filename in filenames:
            filename = filename.split('.')[0]
            names.append(filename)
        print(names)
        return names


def get_achice_id():
    url = 'http://ptms.jlu.edu.cn/ptms/service/res.do'
    data = {"tag": "search@SciAchievement", "branch": "claim", "params": {"name": "", "type": ""}}
    ids = []
    values = execte_url(url, data)['value']
    for value in values:
        id = value['achievement']['achievementId']
        ids.append(id)
    return ids


# 认领成果，这里只是认领了
def add_extra_train_achieve(personAchieveId):
    url = 'http://ptms.jlu.edu.cn/ptms/pAction/extraTrain/add-extra-train-achieve.do'
    data = {"personAchieveId": personAchieveId, "epdId": "42137"}
    execte_url(url, data)
    # ids=get_all_id()
    # for id in ids:
    #     result=submit(id)
    #     print(result)


# 获取认领时提交需要的etaID
def ExtrTrainAchieve():
    etaIDs = []
    url = 'http://ptms.jlu.edu.cn/ptms/service/res.do'
    data = {"tag": "search@ExtrTrainAchieve", "branch": "student", "params": {"name": "", "type": "", "state": ""}}
    values = execte_url(url, data)['value']
    for value in values:
        etaID = value['etaID']
        etaIDs.append(etaID)
    return etaIDs


# 认领后的提交
def submitAfer():
    etaIds = ExtrTrainAchieve()
    url = 'http://ptms.jlu.edu.cn/ptms/pAction/extraTrain/submit-extra-train-achieve.do'
    for etaId in etaIds:
        data = {"etaId": etaId}
        result = execte_url(url, data)
        print(result)
        # print(ExtrTrainAchieve())


ids=get_all_id()
for id in ids:
    result=submit(id)
    print(result)
print(ids)