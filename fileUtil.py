# -*- coding: utf-8 -*-
# @Time : 2021/3/6 23:16
# @Author : Administrator

import time,random

def download(content,path) :
    filename = str(int(time.time())) + str(random.randint(10000, 100000)) + ".jpg"
    f = open(path + filename, "wb")
    f.write(content)
    f.close()