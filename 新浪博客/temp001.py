import requests
import random
import re
import pymongo
import time
from multiprocessing import Pool


url = 'http://comet.blog.sina.com.cn/api?maintype=hits&act=3&uid=15e29f617&ref=http%3A%2F%2Fi.blog.sina.com.cn%2Fblogprofile%2Fprofilelatestnote.php&varname=requestId_23420909'
headers = {
    'Referer': 'http://blog.sina.com.cn/u/5874775575'
}


def view():
    try:
        wb_date = requests.get(url, headers=headers)
        print(wb_date.text)
    except:
        pass


view()