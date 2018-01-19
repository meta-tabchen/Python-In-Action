import requests

url = 'http://www.tabchen.com/ip.php'
proxies={'http':'http://61.130.97.212:8099'}
wb_date = requests.get(url,proxies=proxies)
print(wb_date.text)
