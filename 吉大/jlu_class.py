import requests
import urllib.parse


def request_get(url):
    result = requests.get(url, verify=False)
    # print(result.text)
    return result


def request_post(url):
    result = requests.post(url, verify=False)
    # print(result.text)
    return result


class JluCloud():
    def __init__(self):
        self.mode = "GetUrl"
        self.token = 'xvw3m9amt3aufxihrrwrmu9eez'
        self.files = {}
        self.my_groups = {}
        self.group_id = '9n4ws7zu1m'
        self.local_folder = 'cloud_download'
        self.stack = [""]

    def download(self, file_name):
        file_path = self.files[file_name][0]
        file_path = urllib.parse.quote_plus(file_path)
        url = 'https://api.jlu.meepotech.com/0/groups/{}/roots/meepo/files/%2F{}?token={}&locale=zh_CN'.format(
            self.group_id,
            file_path,
            self.token)
        url = url.replace('+', '%20')
        result = request_get(url)
        f = open(self.local_folder + '/' + file_name, 'wb')
        f.write(result.content)
        f.flush()

    def get_url(self, file_name):
        file_path = self.files[file_name][0]
        file_path = urllib.parse.quote_plus(file_path)
        url = 'http://cloud.jlu.edu.cn/c0/groups/{}/roots/meepo/files/%2F{}?token={}&locale=zh_CN'.format(
            self.group_id,
            file_path,
            self.token)
        url = url.replace('+', '%20')
        print(url)
        # result = request_get(url)
        # f = open(self.local_folder + '/' + file_name, 'wb')
        # f.write(result.content)
        # f.flush()

    def login(self):
        pass

    def myview_updata(self, items):

        pass

    def get_groups(self):
        url = 'https://api.jlu.meepotech.com/0/account/info?offset=0&token={}&locale=zh_CN'.format(self.token)
        url = url.replace('+', '%20')
        result = request_get(url).json()
        groups = result['groups']['groups']
        my_groups = {}
        for one_group in groups[:-1]:
            if (not one_group['relation']['position_str'] == "访问受限的成员"):
                group_name = one_group['group_name']
                group_id = one_group['group_id']
                my_groups[group_name] = group_id
        my_groups['我的空间'] = groups[-1]['group_id']
        self.my_groups = my_groups
        self.myview_updata(self.my_groups.keys())

    def get_files(self, folder_name):

        files = {}
        # print(len(files))
        if (len(self.files) > 0):
            file_path = self.files[folder_name][0]
            self.stack.append(file_path)
            file_path = urllib.parse.quote_plus(file_path)
        else:
            self.stack.append(folder_name)
            file_path = urllib.parse.quote_plus(folder_name)

        url = 'https://api.jlu.meepotech.com/0/groups/{}/roots/meepo/files/%2F{}/meta?list=true&token={}&locale=zh_CN'.format(
            self.group_id, file_path, self.token)
        url = url.replace('+', '%20')
        result = request_get(url).json()
        contents = result['contents']
        for one_conotent in contents:
            path = one_conotent['restore_path'][1:]
            name = one_conotent['name']
            is_dir = one_conotent['is_dir']
            files[name] = [path, is_dir]
        self.files = files
        print(list(self.files.keys()))
        self.myview_updata(self.files.keys())

    def select(self, select_item):
        print(select_item)
        if (self.files[select_item][1]):
            self.get_files(select_item)
        else:
            if (self.mode == "Download"):
                self.download(select_item)
            else:
                self.get_url(select_item)

    def back_last(self):
        self.files = []
        self.stack.pop()
        self.get_files(self.stack.pop())


cloud = JluCloud()
cloud.get_groups()
cloud.group_id = '8xqxn8461p'
cloud.get_files("公开课/国外顶尖大学课程/TED/TED 10")

while True:
    print(cloud.files)
    item = input("input:\n")
    if (item == 'back'):
        cloud.back_last()
    else:
        cloud.select(item)
    print(cloud.stack)
# for i in cloud.files:
#     if (not cloud.files[i][1]):
#         cloud.download(i)
