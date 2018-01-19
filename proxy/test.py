import requests
import json
import time
from bs4 import BeautifulSoup

def getVideo(url):
    proxies = {'https': 'https://117.94.202.179:43700'}
    try:
        # wb_data = requests.get(video, proxies=proxies, headers=headers)

        wb_data = requests.get(url)
        print(wb_data.content)
    except:
        pass


getVideo('http://hhh600.com/html/part/index21_3.html')