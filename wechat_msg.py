# -*- coding: utf-8 -*-
# @Time : 2021/11/7 0:03
# @Author : Administrator
# 指定微信好友 自动发送消息

import pyautogui
import pyperclip
import time,sys

reload(sys)
sys.setdefaultencoding('utf-8')
def get_msg():
     content = u"晚上想吃啥"
     return content
    #return content.split(" ")


def send(msg):
    #复制消息
    pyperclip.copy(msg)
    #模拟键盘 粘贴
    pyautogui.hotkey("ctrl","v")
    #发送消息
    pyautogui.press('enter')

def send_msg(fried):
    # 快捷键打开 微信窗口
    pyautogui.hotkey("ctrl","alt","w")
    #搜索 好友
    pyautogui.hotkey("ctrl","f")
    #复制好友昵称到 粘贴板
    pyperclip.copy(fried)
    #模拟键盘 粘贴文件传输助手

    pyautogui.hotkey("ctrl", "v")
    #沉睡2秒文件传输助手

    time.sleep(2)
    #回车进入好友消息页面文件传输助手

    pyautogui.hotkey("enter")
    #一条一条发消息
    for msg in get_msg():
        send(msg)
        time.sleep(2)

if __name__ == '__main__':
    friend_name = "文件传输助手"

    send_msg(friend_name)
    #文件传输助手
    # print get_msg()