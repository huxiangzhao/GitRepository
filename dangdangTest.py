# -*- coding: utf-8 -*-
# @Time : 2021/3/6 20:51
# @Author : Administrator
# 下载当当网图片

import requests
from bs4 import BeautifulSoup
import fileUtil

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def getPic(path,url) :
    #url = "http://search.dangdang.com/?key=%C1%AC%D2%C2%C8%B9&act=input&page_index=1"
    res = requests.get(url,headers=headers)
    #print res.content
    soup = BeautifulSoup(res.content,"html.parser")

    arr = soup.find_all("img")
    for i in arr :
        try :
            img_url = i["src"]
        except Exception :
            continue
        else :
            if (not str(img_url).startswith("//")) | (len(str(img_url).split("_"))<=2) :
                continue
            print img_url
            res2 = requests.get("http:"+img_url)

            fileUtil.download(res2.content,path)


for i in range(1,20) :
    url = "http://search.dangdang.com/?key=%C1%AC%D2%C2%C8%B9&act=input&page_index="+str(i)
    #getPic("G:\\aaa\\",url)
    getPic("G:\\ceshi\\dangdang\\",url)