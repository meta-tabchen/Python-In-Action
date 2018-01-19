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
group_id = '9n4ws7zu1m'
group = tabchen_master
files = {}
my_groups = {}


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


def get_groups():
    url = 'https://api.jlu.meepotech.com/0/account/info?offset=0&token={}&locale=zh_CN'.format(token)
    result = request_get(url).json()
    groups = result['groups']['groups']

    for one_group in groups:
        if (not one_group['relation']['position_str'] == "访问受限的成员"):
            group_name = one_group['group_name']
            group_id = one_group['group_id']
            my_groups[group_name] = group_id
    return list(my_groups.keys()), my_groups


def get_files(folder_name):
    folder_name = urllib.parse.quote_plus(folder_name)
    url = 'https://api.jlu.meepotech.com/0/groups/{}/roots/meepo/files/%2F{}/meta?list=true&token={}&locale=zh_CN'.format(
        group_id, folder_name, token)
    result = request_get(url).json()
    contents = result['contents']
    for one_conotent in contents:
        path = one_conotent['restore_path'][1:]
        name = one_conotent['name']
        is_dir = one_conotent['is_dir']
        files[name] = [path, is_dir]
    print(list(files.keys()))
    return list(files.keys())


def download(file_name):
    file_path = files[file_name][0]
    file_path = urllib.parse.quote_plus(file_path)
    url = 'https://api.jlu.meepotech.com/0/groups/{}/roots/meepo/files/%2F{}?token={}&locale=zh_CN'.format(group_id,file_path,token)
    result = request_get(url)
    f=open(file_name,'wb')
    f.write(result.content)
    f.flush()


def select(select_item):
    print(select_item)
    if (files[select_item][1]):
        get_files(select_item)
    else:
        download(select_item)


file = get_files('ipad')
print(files)
print(select(file[0]))
# get_master()
