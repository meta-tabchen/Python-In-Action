import requests
url='http://hackdata.cn/learn/course/2/lecture/111/'



cookies = 'UM_distinctid=15bf5e3539a214-0c80f9d2338def-57e143d-1fa400-15bf5e3539b121; sessionid=98kzhxj3rh62mtp0oej7ulzxvk1nd9qu; CNZZDATA1260061217=1781353524-1494474680-%7C1496096548'

headers={'Cookie':cookies}
wb_data=requests.get(url,headers=headers)
print(wb_data.text)