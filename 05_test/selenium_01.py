#!/usr/bin/env python
'''
http://selenium-python.readthedocs.io/api.html#locate-elements-by

'''
import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 01. Basic setting
#binary = os.path.join('C:\home\dev\workspace_python\python_test\driver','chromedriver.exe')
binary = 'C:\home\dev\workspace_python\python_test\driver\chromedriver.exe'
browser = webdriver.Chrome(binary)
time.sleep(1)

# 02. Connection
browser.get('http://www.bigfile.co.kr/sso/sso_user_login.php')

# 03. Account settings
time.sleep(1)
search = browser.find_element_by_name('userid')
search.send_keys('rootguy')
search = browser.find_element_by_name('password')
search.send_keys('fmam0507')
search.send_keys(Keys.RETURN)

# 04. Participate in the svent
time.sleep(1)
browser.get('http://www.bigfile.co.kr/event/2014_stamp/main.php')
time.sleep(1)
search = browser.find_element_by_class_name('chul_link')
search.click();

# 05. End2
time.sleep(5)
browser.quit()