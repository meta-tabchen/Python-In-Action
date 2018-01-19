from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://passport.baidu.com/center")
driver.delete_all_cookies()
cookies = 'BAIDUID=3A109F5D9606C632807C9110D6A28022:FG=1; BIDUPSID=3A109F5D9606C632807C9110D6A28022; PSTM=1489497601; HOSUPPORT=1; UBI=fi_PncwhpxZ%7ETaL96JyDH3lMrLTTGwiJx2oZuAXlPK6kbKhGYXSkhpvJclg2es9BXtXikQeUQogVMU6eXbCbGna4eGWfelt7nvbd4O-0w8AVWQS-PADYeBdz6k9B8QwQ3iHaHS0QOnpQx12kgRxiVCafuFiIg__; HISTORY=29f794d245bc14c5858ce426cf2768c16f1f54; BDUSS=HNtc2Q1NWMwb1pXSXB5dXdpWVRuRnpDWkVvalg2MlhadnlKbXl3SlBnN0RvdkJZSVFBQUFBJCQAAAAAAAAAAAEAAACu0Jp1VGFiQ2hlbmpsdQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMMVyVjDFclYN; SAVEUSERID=8a330866a3bcc2d666de85d03dde5f; USERNAMETYPE=3; PTOKEN=88d98acc3aa5b42121a4c2190c968099; STOKEN=8a4eb9e0b37d0d979eb56e13da8293401346f35231433b76ac067c8353eb071b; MCITY=-53%3A; __cfduid=dfff9c983e58335f718d4b1e7237649f71494066721; H_PS_PSSID=22161_1437_21121_20882_22159; FP_UID=66a0712cc17fb0e3b458966b5c61604d'
cookies = cookies.split(';')

for cookie in cookies:
    cookie = cookie.split('=')
    cookie = {
        'value': cookie[1].strip(), 'name': cookie[0].strip()
    }
    driver.add_cookie(cookie)
    print(cookie)
time.sleep(3)
driver.get("https://passport.baidu.com/center")
