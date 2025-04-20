# -*- coding: utf-8 -*-
# @Time : 2021/3/6 18:50
# @Author : Administrator

import requests
from bs4 import BeautifulSoup
import fileUtil

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
def getPic(path,url):

    res = requests.get(url,headers=headers)

    soup = BeautifulSoup(res.content,"lxml")
    img_soup = soup.find_all("img")

    for img_url in img_soup :
        try :
            img = img_url.attrs["data-original"]
        except Exception:
            continue
        else:
            result = requests.get(img)
            print "download " + img
            fileUtil.download(result.content,path)
            #filename = str(int(time.time()))+str(random.randint(10000,100000)) + ".jpg"
            # print "download "+ img
            # f = open(path + filename, "wb")
            # f.write(result.content)
            # f.close()

    ##print div_soup

# def download(content,path) :
#     filename = str(int(time.time())) + str(random.randint(10000, 100000)) + ".jpg"
#     f = open(path + filename, "wb")
#     f.write(content.content)
#     f.close()

for i in range(1,20) :
    url = "https://pic88.com/photo/ameinv-d"+str(i)+"-o0-p0"
    getPic("G:\\aaa\\",url)