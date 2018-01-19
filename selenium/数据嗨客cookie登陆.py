from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url='http://hackdata.cn/'
driver.get(url)

# log = driver.find_element_by_class_name('login-no').click()


cookies = 'UM_distinctid=15bf5e3539a214-0c80f9d2338def-57e143d-1fa400-15bf5e3539b121; sessionid=98kzhxj3rh62mtp0oej7ulzxvk1nd9qu; CNZZDATA1260061217=1781353524-1494474680-%7C1496096548'

cookies = cookies.split(';')
driver.delete_all_cookies()

for cookie in cookies:
    cookie = cookie.split('=')
    cookie = {
        'value': cookie[1].strip(), 'name': cookie[0].strip()
    }
    driver.add_cookie(cookie)
driver.get('http://hackdata.cn/learn/')

courses=driver.find_elements_by_class_name('listmove')
courses[0].click()
time.sleep(2)
driver.back()
courses[1].click()
