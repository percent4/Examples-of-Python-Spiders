# -*- coding: utf-8 -*-

# 本爬虫利用Selenium+AutoIt实现功能： 往百度网盘上传文件
# 需要读者掌握AutoIt方面的知识
# import modules
import os
import time
from selenium import webdriver
from selenium.common.exceptions import *

# 启动Chrome浏览器
browser = webdriver.Chrome()
print("浏览器已启动......")

# 加载百度网盘网页，如果加载时间超过60s,就停止加载网页
url = 'https://pan.baidu.com/'
#browser.maximize_window() #窗口最大化
browser.set_page_load_timeout(60) # 最大等待时间为30s
try:
    browser.get(url)
except TimeoutException:
    browser.execute_script('window.stop()')

time.sleep(10)
# 找到“账号密码登录”，并点击
browser.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn").click()
print('使用账号密码登录......')
time.sleep(2)

# 从本地txt文件中获取百度网盘的账号和密码
with open("E://baidu_disk.txt",'r') as f:
    username,password = f.read().split()

# 输入账号、密码，并点击“登录按钮”
browser.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(username)
browser.find_element_by_id("TANGRAM__PSP_4__password").send_keys(password)
browser.find_element_by_id("TANGRAM__PSP_4__submit").click()
time.sleep(15)

# 使用AuotIt生成的exe实现文件上传
print('正在上传文件中......')
os.system(r'E:\upload_file.exe')
print('上传文件成功！')

# 关闭浏览器
time.sleep(15)
browser.quit()
