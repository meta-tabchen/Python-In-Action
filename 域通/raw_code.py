import requests
import re
import time
import random


def execute_url(url):
    wb_data = requests.get(url, verify=False)
    return wb_data.json()


def get_home_file(url='https://chenfutu.ctfile.com/u/13762377'):
    urlsplit = url.split('/')
    uid = urlsplit[4]
    host = 'https://' + urlsplit[2]
    header = {'Connection': 'keep-alive'}

    wb_data = requests.get(url, headers=header, verify=False)

    unique_id = wb_data.headers['Set-Cookie'].split(';')[0]
    unique_id = unique_id.split('=')[-1]
    url = host + re.findall('"sAjaxSource": "(.+)"', wb_data.text)[
        0] + '&iSortingCols=1&bSortable_0=false&bSortable_1=true&bSortable_2=true&bSortable_3=true'
    aaData = execute_url(url)['aaData']
    items = []
    for one_data in aaData:
        value = re.findall('value="(.+?)"', one_data[0])[0]
        filename = re.findall('<a.+?>(.+?)<', one_data[1])[0]
        item_type = 'file'
        if 'folder' in re.findall('name="(.+?)"', one_data[0])[0]:
            item_type = 'folder'
        item = {'name': filename, 'value': value, 'type': item_type}
        items.append(item)
    return items, uid, unique_id


# get_home_file('https://chenfutu.ctfile.com/u/13762377/20621609')


def get_file_url():
    host = 'https://chenfutu.ctfile.com'
    # 先获取总文件数然后获取所有的文件链接
    file_urls = []
    file_names = []
    file_ids = []
    folder_id = '21083441'
    url = 'http://chenfutu.ctfile.com/iajax_guest.php?item=file_act&action=file_list&folder_id={}&uid=13762377&display_subfolders=0&t=1510410200&k=b1fb681fc421abef4f1287ee80bbf1ca&iDisplayStart=0&iDisplayLength=0'.format(
        folder_id)
    wb_data = execute_url(url)
    print('wwwwwwwww')
    iTotalRecords = wb_data['iTotalRecords']
    new_url = 'https://chenfutu.ctfile.com/iajax_guest.php?item=file_act&action=file_list&folder_id={}&uid=13762377&display_subfolders=0&t=1510410200&k=b1fb681fc421abef4f1287ee80bbf1ca&iDisplayStart=0&iDisplayLength={}&iSortCol_0=3&sSortDir_0=desc&iSortingCols=1&bSortable_0=false&bSortable_1=true&bSortable_2=true&bSortable_3=true'.format(
        folder_id, iTotalRecords)
    allData = execute_url(new_url)['aaData']
    for one_data in allData:
        key = one_data[0]
        file_id = re.findall('value="(.+?)"', key)[0]
        key = one_data[1]
        file_url = host + re.findall('href="(.+?)"', key)[0]
        file_name = re.findall('<a.+>(.+)</a>', key)[0]
        file_urls.append(file_url)
        file_names.append(file_name)
        file_ids.append(file_id)
        # print(len(allData)
    return file_names, file_urls, file_ids


def get_detail_url(file_id='173655804', user_id="13762377"):
    url = 'https://chenfutu.ctfile.com/guest_loginV3.php'
    data = "file_id={}&userid={}".format(file_id, user_id)
    header = {'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        , 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q={}'.format(str(random.random()))}
    wb_data = requests.post(url, headers=header, data=data, verify=False)

    # wb_data = requests.get(url, headers=header, verify=False)
    url = re.findall("free_down_action\('(.+?)'", wb_data.text)[0]
    return url
    # print(wb_data.content)


def download(url, filename="temp.pdf"):
    print(filename, 'is start')
    wb_data = requests.get(url)
    # print(wb_data.text)
    f = open(filename, "wb")
    f.write(wb_data.content)
    print(filename, "download over")


def start(url):
    items, uid, unique_id = get_home_file(url)
    furls = open('urls.txt', 'w')
    fnames = open('names.txt', 'w')
    for item in items:
        print(item)
        file_id = item['value']
        file_name = item['name']
        fnames.write(file_name)
        fnames.write('\n')
        fnames.flush()
        # f=open('last','w')
        # f.write(file_name)
        print(file_id, uid, unique_id)
        url = get_detail_url(file_id, uid)
        furls.write(url)
        furls.write('\n')
        furls.flush()
        # download(url, file_name)
        # f.write(file_names)

        # start()
        # get_file_url()
        # get_home_file()
        time.sleep(2)


if __name__ == '__main__':
    start('https://n95003.ctfile.com/u/15796230/25842447')
