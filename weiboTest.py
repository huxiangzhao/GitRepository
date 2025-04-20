# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0:03
# @Author : Administrator

import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
           'cookie':'SINAGLOBAL=4212779017760.9746.1520070886058; SUB=_2AkMXGHqcf8NxqwJRmPEczWPhao91zw3EieKhRItHJRMxHRl-yj9kqlIstRB6PJhUc1sDUiB3A1txydDbEbqLBadzx7pP; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WF4KLZWVUqxM2L_8.FMlMZr; ULV=1615132076913:7:1:1:1116622260955.2378.1615132076908:1595743541815; XSRF-TOKEN=2ICV4WYZCzEPGdeAF65uEiIw; WBPSESS=IawIaCISeX-46VmeRocrJ-SZX3oggrQN6RKD0_3HcexK8sKVni4n6tBQJ_HkGn2kZgGdOabmRLF8ENrNEp6tGeDIHXqyTiDPItUmQR1tUllRDAYEBC80bfxFcyqfu3_u'}
cookie = ""

def getVideoUrl():
    url = "https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=0&group_id=102803&containerid=102803&extparam=discover%7Cnew_feed&max_id=0&count=10"
    res = requests.get(url,headers)
    print res.content
    print res.cookies



getVideoUrl()