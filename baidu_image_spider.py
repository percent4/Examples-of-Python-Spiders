# -*- coding: utf-8 -*-

# 本爬虫利用selenium的Chromedriver下载图片
# 导入模块
import time
import datetime
from selenium import webdriver
from selenium.common.exceptions import *

# 启动Chrome浏览器
driver = webdriver.Chrome()
print('浏览器已启动.')

# 设置超时时间
# 加载百度图片网页，若超过30秒就停止加载
driver.set_page_load_timeout(30)
try:
    driver.get('http://image.baidu.com/')
except TimeoutException:
    driver.execute_script('window.stop()')

# 在输入框中输入'新垣结衣',并查询
driver.find_element_by_id('kw').send_keys('新垣结衣')
driver.find_element_by_class_name('s_search').click()
driver.implicitly_wait(30)

# 利用css_selector找到第一张图片，并单击
first_img = driver.find_element_by_css_selector('.main_img.img-hover')
first_img.click()
driver.implicitly_wait(30)
# 窗口句柄切换到新窗口
driver.switch_to_window(driver.window_handles[1])

print('开始下载图片.')
# 下载100张图片，可以自己控制图片数量
for _ in range(100):

    try:
        time.sleep(5)
        # 点击下载图片按钮
        driver.find_element_by_xpath('//*[@id="toolbar"]/span[7]').click()
    except TimeoutException:
        print('超时')
        driver.execute_script('window.stop()')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="toolbar"]/span[7]').click()
    except ElementNotVisibleException:
        print('元素不存在')
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="toolbar"]/span[7]').click()
    except Exception:
        print('第%d张图片下载失败.'%_)

    time.sleep(2)
    print('第%d张图片下载成功.' % (_ + 1))
    # 点击下一张按钮
    driver.find_elements_by_class_name('img-switch-btn')[1].click()
    time.sleep(2)


time.sleep(10)
driver.quit()
print('图片下载完毕！')

