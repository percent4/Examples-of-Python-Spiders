# -*- coding: utf-8 -*-

# 本爬虫利用selenium的PhantomJ或Chromedriver爬取手机号码信息
# 导入模块
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import *

# 开始时间
d1 = datetime.datetime.now()

# 配置浏览器加载项
service_args=[]
service_args.append('--load-images=no')  ##关闭图片加载
driver = webdriver.PhantomJS(service_args=service_args)
#driver = webdriver.Chrome(service_args=service_args)

# 设置超时时间，若超过15秒就停止加载
driver.set_page_load_timeout(15)
try:
    driver.get('https://www.baidu.com')
except TimeoutException:
    driver.execute_script('window.stop()')

# 手机号码列表
phone_list = ['13162659020','15921925731','18768144196','18729768543','18669683228','057126883245',\
              '18762144200','07922248454','15225403490']

#对每个手机号进行爬取
for phone in phone_list:
    try:
        # 找到输入框，并输入手机号码
        driver.find_element_by_id('kw').send_keys(phone)
        # 找到“百度一下按钮”，并点击
        driver.find_element_by_id('su').click()
        # 刷新网页
        driver.refresh()
        # 隐式等待10秒
        driver.implicitly_wait(10)

        # 获取网页源代码
        source = driver.page_source
        # 利用BeautifulSoup解析网页
        soup = BeautifulSoup(source, 'lxml')
        # 获取手机号码相关信息
        text = soup.find('div', class_="op_fraudphone_row")
        # 提出HTML标签中的文字并输出
        phone_info = text.text
        print(phone_info)
    except BaseException:
        pass
    finally:
        # 网页后退
        driver.back()
        driver.implicitly_wait(10)

# 关闭浏览器窗口
driver.quit()

# 结束时间和花费时间
d2 = datetime.datetime.now()
print('Cost time:%s'%(d2-d1))
