# -*- coding: utf-8 -*-
# @Time : 2022/3/23 23:09
# @Author : Administrator
#爬取国家统计局  省市区街道 数据

import sys
import requests
from bs4 import BeautifulSoup
import fileUtil
reload(sys)
sys.setdefaultencoding('utf-8')
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

#获取省份信息
def getProvince():
    url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2021/"
    res = requests.get(url)
    print res.content
    soup = BeautifulSoup(res.content, "html.parser",from_encoding='utf8')
    arr = soup.find_all("a")
    for i in arr:

        href = i["href"]
        if(str(href).endswith("html")):
            provinceCode =  str(href).split(".")[0] + "0000000000"
            provinceName = i.contents[0]
            print provinceCode+"::::::"+provinceName
            # print "province:" + i.contents[0]
            # print "provinceCode:"+str(href).split(".")[0]+"0000000000"
            getCity(url,str(href),provinceName,provinceCode)

#获取市信息
def getCity(url,city_href,provinceName,provinceCode):
    res = requests.get(url+city_href)
    soup = BeautifulSoup(res.content, "html.parser")

    arr1 = soup.find_all("tr",attrs={'class':'citytr'})

    # print arr1
    for i in arr1:

        city = i.find_all("a")
        if(u"市辖区".__eq__(city[1].text)):
            print city[0].text + "::::::" + provinceName+"辖区"+":::parent:::"+provinceCode
        else:
            print city[0].text + "::::::" + city[1].text+":::parent:::"+provinceCode
        href = city[0]["href"]
        # print href

        getCounty(url , href, city[1].text, city[0].text)


    # arr = soup.find_all("a")
    # for i in arr:
    #     href = i["href"]
    #     if(str(href).endswith("html")):
    #         if(u"市辖区".__eq__(i.contents[0])):
    #             print "city1:" + province
    #         else:
    #             print "city:" + i.contents[0]

            #print href




#获取区(县)信息
def getCounty(url,county_href,city_name,city_code):
    res = requests.get(url + county_href)
    soup = BeautifulSoup(res.content, "html.parser")

    arr1 = soup.find_all("tr", attrs={'class': 'countytr'})

    # print arr1
    for i in arr1:
        #print i.td[2].text
        county_filter = i.find_all("td")
        #if(county.size)
        if (u"市辖区".__eq__(county_filter[1].text)):
            print u"过滤:"+county_filter[0].text+":::"+county_filter[1].text
            continue
        county = i.find_all("a")
        county_code= county[0].text
        county_name = county[1].text
        if (u"市辖区".__eq__(county_name)):
            print county_code + "::::::" + city_name + "辖区" + ":::parent:::" + city_code
        else:
            print county_code + "::::::" + county_name + ":::parent:::" + city_code


if __name__ == '__main__':

    getProvince()