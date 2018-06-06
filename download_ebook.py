# -*- coding:utf-8 -*-
# 本爬虫读取已写入txt文件中的电子书的链接，并用多线程下载

import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import urllib.request

# 利用urllib.request.urlretrieve()下载PDF文件
def download(url):
    # 书名
    book_name = 'E:\\Ebooks\\'+url.split('/')[-1]
    print('Downloading book: %s'%book_name) # 开始下载
    urllib.request.urlretrieve(url, book_name)
    print('Finish downloading book: %s'%book_name) #完成下载

def main():
    start_time = time.time() # 开始时间

    file_path = 'E:\\Ebooks\\book.txt' # txt文件路径
    # 读取txt文件内容，即电子书的链接
    with open(file_path, 'r') as f:
        urls = f.readlines()
    urls = [_.strip() for _ in urls]

    # 利用Python的多线程进行电子书下载
    # 多线程完成后，进入后面的操作
    executor = ThreadPoolExecutor(len(urls))
    future_tasks = [executor.submit(download, url) for url in urls]
    wait(future_tasks, return_when=ALL_COMPLETED)

    # 统计所用时间
    end_time = time.time()
    print('Total cost time:%s'%(end_time - start_time))

main()