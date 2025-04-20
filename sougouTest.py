# -*- coding: utf-8 -*-
# @Time : 2021/3/6 13:40
# @Author : Administrator

import requests
import json
#import urllib

#import bs4 from BeautifulSoup

def getSougouImg(path) :
    url = "https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?" \
          "category=%E5%A3%81%E7%BA%B8&tag=%E5%85%A8%E9%83%A8&start=0&len=2000"
    #访问url
    res = requests.get(url)
    #该网址图片属于动态加载内容   返回为json格式
    json_result = json.loads(res.text)
    #转成json 获取节点
    arr = json_result["all_items"]
    #imgs_url = []
    #将图片路径放置到数组中

    m = 0
    for i in arr :
        imgs_url = i["sthumbUrl"]
        print('***** ' + str(m) + '.jpg *****' + '   Downloading...')
        res = requests.get(imgs_url)
        filename = str(m)+".jpg"
        f = open(path+filename,"wb")
        f.write(res.content)
        f.close()
        #urllib.request.urlretrieve(imgs_url,path+str(m)+'.jpg')
        m = m + 1

    #print arr



getSougouImg("G:\\aaa\\")