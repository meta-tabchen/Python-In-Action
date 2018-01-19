from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("http://hackdata.cn/")

log=driver.find_element_by_class_name('login-no').click()



user=driver.find_element_by_id('id_username')
password=driver.find_element_by_id('id_password')
check=driver.find_element_by_id('id_captcha_1')
submit=driver.find_element_by_class_name('login-btn')


key=input()
user.send_keys('haoyongle')
password.send_keys('plkjplkj')
check.send_keys(str(key))
submit.click()
time.sleep(2)
cookie=driver.get_cookie()
print(cookie)
