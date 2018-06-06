# -*- coding:utf-8 -*-
# 本爬虫用来下载http://www.allitebooks.com/中的电子书
# 本爬虫将需要下载的书的链接写入txt文件，便于永久使用
# 网站http://www.allitebooks.com/提供编程方面的电子书

#  导入必要的模块
import urllib.request
from bs4 import BeautifulSoup

#  获取网页的源代码
def get_content(url):
    html = urllib.request.urlopen(url)
    content = html.read().decode('utf-8')
    html.close()
    return content

# 将762个网页的网址储存在list中
base_url = 'http://www.allitebooks.com/'
urls = [base_url]
for i in range(2, 762):
    urls.append(base_url + 'page/%d/' % i)

# 电子书列表，每一个元素储存每本书的下载地址和书名
book_list =[]

# 控制urls的数量,避免书下载过多导致空间不够!!!
# 本例只下载前3页的电子书作为演示
# 读者可以通过修改url[:3]中的数字,爬取自己想要的网页书，最大值为762
for url in urls[:1]:
    try:
        # 获取每一页书的链接
        content = get_content(url)
        soup = BeautifulSoup(content, 'lxml')
        book_links = soup.find_all('div', class_="entry-thumbnail hover-thumb")
        book_links = [item('a')[0]['href'] for item in book_links]
        print('\nGet page %d successfully!' % (urls.index(url) + 1))
    except Exception:
        book_links = []
        print('\nGet page %d failed!' % (urls.index(url) + 1))

    # 如果每一页书的链接获取成功
    if len(book_links):
        for book_link in book_links:
            # 下载每一页中的电子书
            try:
                content = get_content(book_link)
                soup = BeautifulSoup(content, 'lxml')
                # 获取每本书的下载网址
                link = soup.find('span', class_='download-links')
                book_url = link('a')[0]['href']

                # 如果书的下载链接获取成功
                if book_url:
                    # 获取书名
                    book_name = book_url.split('/')[-1]
                    print('Getting book: %s' % book_name)
                    book_list.append(book_url)
            except Exception as e:
                print('Get page %d Book %d failed'
                      % (urls.index(url) + 1, book_links.index(book_link)))

# 文件夹
directory = 'E:\\Ebooks\\'
# 将书名和链接写入txt文件中，便于永久使用
with open(directory+'book.txt', 'w') as f:
    for item in book_list:
        f.write(str(item)+'\n')

print('写入txt文件完毕!')