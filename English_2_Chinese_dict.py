import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
import random
import ctypes

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_DARKBLUE = 0x01  # 暗蓝色
FOREGROUND_DARKGREEN = 0x02  # 暗绿色
FOREGROUND_DARKSKYBLUE = 0x03  # 暗天蓝色
FOREGROUND_DARKRED = 0x04  # 暗红色
FOREGROUND_DARKPINK = 0x05  # 暗粉红色
FOREGROUND_DARKYELLOW = 0x06  # 暗黄色
FOREGROUND_DARKWHITE = 0x07  # 暗白色
FOREGROUND_DARKGRAY = 0x08  # 暗灰色
FOREGROUND_BLUE = 0x09  # 蓝色
FOREGROUND_GREEN = 0x0a  # 绿色
FOREGROUND_SKYBLUE = 0x0b  # 天蓝色
FOREGROUND_RED = 0x0c  # 红色
FOREGROUND_PINK = 0x0d  # 粉红色
FOREGROUND_YELLOW = 0x0e  # 黄色
FOREGROUND_WHITE = 0x0f  # 白色

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

def resetColor():
    set_cmd_text_color(FOREGROUND_DARKWHITE)


def cprint(mess, color):
    color_dict = {'暗蓝色': FOREGROUND_DARKBLUE,
                  '暗绿色': FOREGROUND_DARKGREEN,
                  '暗天蓝色': FOREGROUND_DARKSKYBLUE,
                  '暗红色': FOREGROUND_DARKRED,
                  '暗粉红色': FOREGROUND_DARKPINK,
                  '暗黄色': FOREGROUND_DARKYELLOW,
                  '暗白色': FOREGROUND_DARKWHITE,
                  '暗灰色': FOREGROUND_DARKGRAY,
                  '蓝色': FOREGROUND_BLUE,
                  '绿色': FOREGROUND_GREEN,
                  '天蓝色': FOREGROUND_SKYBLUE,
                  '红色': FOREGROUND_RED,
                  '粉红色': FOREGROUND_PINK,
                  '黄色': FOREGROUND_YELLOW,
                  '白色': FOREGROUND_WHITE
                 }
    set_cmd_text_color(color_dict[color])
    print(mess)
    resetColor()

color_list = ['暗蓝色','暗绿色','暗天蓝色','暗红色','暗粉红色','暗黄色','暗白色','暗灰色',\
              '蓝色','绿色','天蓝色','红色','粉红色','黄色','白色']

# print information of this application
print('#'*60)
print('This app is used for translating English word to Chineses!')
print('#'*60+'\n')

# get word from Command line
word = input("Enter a word (enter 'q' to exit): ")

# main body
while word != 'q': # 'q' to exit
    try:
        # 利用GET获取输入单词的
        r = requests.get(url='http://dict.youdao.com/w/%s/#keyfrom=dict2.top'%word)
        # 利用BeautifulSoup将获取到的文本解析成HTML
        soup = BeautifulSoup(r.text, "lxml")

        # 获取字典的标签内容
        s = soup.find(class_='trans-container')('ul')[0]('li')
        # 选择输出的颜色
        random.shuffle(color_list)
        # 输出字典的具体内容
        for item in s:
            if item.text:
                cprint(item.text, color_list[0])
        print('='*40+'\n')
    except Exception:
        print("Sorry, there is a error!\n")
    finally:
        word = input( "Enter a word (enter 'q' to exit): ")