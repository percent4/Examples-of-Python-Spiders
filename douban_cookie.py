# 本爬虫利用Cookie登录豆瓣账号，并获取该账号的昵称
# 只需要输入自己的豆瓣账号和密码即可

import os
import urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup

# 如果douban_login.txt不存在，则利用cookie登录豆瓣账号，
# 并把登陆后的页面HTML源码写入douban_login.txt
if not os.path.exists('E://douban_login.txt'):

    # 登录网址
    url = "https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001"
    # 输入账号、密码
    postdata = urllib.parse.urlencode({
        "form_email": "15921925731", # 自己的账号
        "form_password": "******"    # 自己的密码
    }).encode("utf-8")

    # 创建Request
    req = urllib.request.Request(url, postdata)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36")

    # 使用http.cookiejar.CookieJar()创建CookieJar对象
    cjar = http.cookiejar.CookieJar()

    # 使用HTTPCookieProcessor创建cookie处理器，并以其参数构建opener对象
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
    # 将opener安装为全局
    content = opener.open(req).read().decode()

    # 把登陆后的页面HTML源码写入douban_login.txt
    with open('E://douban_login.txt', 'w') as f:
        f.write(content)

# 如果douban_login.txt存在，则读取里面的内容
else:

    # 读取douban_login.txt的内容
    with open('E://douban_login.txt', 'r') as f:
        content = f.read()
    # 利用BeautifulSoup将文本解析成HTML
    soup = BeautifulSoup(content, 'lxml')

    # 获取账号信息
    a = soup.find('a', class_='bn-more')
    username = a.text.replace('的帐号', '')
    print('您的豆瓣昵称是%s'%username)