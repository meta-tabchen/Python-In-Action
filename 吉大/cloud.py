import requests
import urllib.parse
import os, glob
import time

xia_token = 'xc9uqzau2iv4v2rqjsx5iscryq'
my_token = 'xvw3m9amt3aufxihrrwrmu9eez'
token = my_token

import time

tabchen_group = '23y5p84gqi'
tabchen_master = '9n4ws7zu1m'
xia_master = 'zksu7zs7dj'
group = tabchen_master


# coding=utf-8

def File_md5(filename):
    import hashlib
    import os  # Python os模块包含普遍的操作系统功能。如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。
    _FILE_SLIM = 100 * 1024 * 1024
    calltimes = 0  # 分片的个数
    hmd5 = hashlib.md5()
    fp = open(filename, "rb")
    f_size = os.stat(filename).st_size  # 得到文件的大小
    if f_size > _FILE_SLIM:
        while (f_size > _FILE_SLIM):
            hmd5.update(fp.read(_FILE_SLIM))
            f_size /= _FILE_SLIM
            calltimes += 1  # delete    #文件大于100M时进行分片处理
        if (f_size > 0) and (f_size <= _FILE_SLIM):
            hmd5.update(fp.read())
    else:
        hmd5.update(fp.read())
    return (hmd5.hexdigest(), calltimes)


def request_get(url):
    result = requests.get(url, verify=False)
    # print(result.text)
    return result


def request_post(url):
    result = requests.post(url, verify=False)
    # print(result.text)
    return result


def login(user_name, password):
    url = 'https://api.jlu.meepotech.com/0/account/login?user_name={}&password={}&device_name=Android%3AXT1581&locale=zh_CN'.format(
        user_name, password)
    result = request_post(url)
    print(result.text)


def get_master():
    url = 'https://api.jlu.meepotech.com/0/account/info?offset=0&token={}&locale=zh_CN'.format(token)
    result = request_get(url).json()
    print(result['user_id'])
    return result['user_id']


def upload(path, folder='upload'):
    folder = folder.replace('\\', '/')
    try:
        if (folder[-1] != '/'):
            folder = folder + '/'
    except:
        pass
    fliename = path.split('/')[-1]
    print(fliename)
    file_url = urllib.parse.quote_plus((folder + fliename))  # 这里使用quote_plus()不然'/'不会被编码
    # print(file_url)
    upload_url = 'https://api.jlu.meepotech.com/0/groups/{}/chunked_upload?offset=0&token={}&locale=zh_CN'.format(
        group,
        token)
    file = open(path, 'rb')
    wb_data = requests.post(upload_url, data=file, verify=False).json()
    upload_id = wb_data['upload_id']

    url = 'https://api.jlu.meepotech.com/0/groups/{}/roots/meepo/files/%2F{}/commit_chunked_upload?upload_id={}&modified={}&token={}&locale=zh_CN'.format(
        group, file_url, upload_id, int(time.time() * 1000), token)
    request_post(url)


# upload("test_big2.rar")
def upload_foler(path):
    path = path.replace('\\', '/')
    # print(path)
    if (path[-1] != '/'):
        path = path + '/'
    # print(path)
    for i in glob.glob(path + '*'):
        if (os.path.isfile(i)):
            filename = i.split('\\')[-1]
            print(filename, path)


def rename_folder(oldname, newname):
    oldname_url = urllib.parse.quote_plus(oldname)
    newname_url = urllib.parse.quote_plus(newname)
    url = 'https://api.jlu.meepotech.com/0/groups/{}/roots/meepo/files/%2F{}/move?to_path=%2F{}&token={}&locale=zh_CN'.format(
        group, oldname, newname, token)
    request_post(url)


# 这里会把整个文件夹删除
def delete_folder(folder_name):
    folder_name_url = urllib.parse.quote_plus(folder_name)
    url = 'https://api.jlu.meepotech.com/0/groups/{}/roots/meepo/files/%2F{}/trash?token={}&locale=zh_CN'.format(
        group, folder_name_url, token)
    request_post(url)


def create_folder(folder_name):
    folder_name_url = urllib.parse.quote_plus(folder_name)
    url = 'https://api.jlu.meepotech.com/0/groups/{}/roots/meepo/files/%2F{}/create_folder?token={}&locale=zh_CN'.format(
        group, folder_name_url, token)
    request_post(url)


# create_folder('hello')
# rename_folder('hello', '你好')
# delete_foler('你好')

def get_folder_path(path, master_folder):

    loc = path.find(master_folder)
    if(loc==-1):
        return master_folder
    # print(loc)
    path = path[loc:]
    temp = path.split('/')[-1]
    loc = path.find(temp)
    path = path[:loc]
    print(path)
    return path


f = open('md5.log', 'w')


def get_all(path, master_folder):
    path = path.replace('\\', '/')
    try:
        if (path[-1] != '/'):
            path = path + '/'
    except:
        pass
    print('当前上传的文件夹是>>>>>', path)

    for now in glob.glob(path + '*'):
        now = now.replace('\\', '/')
        if (os.path.isdir(now)):
            get_all(now, master_folder)

        else:
            try:
                upload(now, get_folder_path(now, master_folder))
            except:
                print('error>>>>>', now, get_folder_path(now, master_folder))
                # print(get_folder_path(now, master_folder))


# upload('go.pdf','video/vieo')
get_all("E:\FTP\Linux书籍", '书籍')
# # delete_folder('upload/go.pdf')
# files = {'one': '1', 'two': '2', 'three': '3'}
# items = ['one', 'two']
# c = [x for x in list(files.keys()) if x not in items]
# files.pop()
# print(c)
