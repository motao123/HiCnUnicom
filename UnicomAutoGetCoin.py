
# coding=utf-8
# author:@QiuYueBai

import http.cookiejar
import json
import os
import sys
import urllib.request as urllib2
import ssl
import urllib
import datetime
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
class Qiandao():

    def __init__(self):
        self.cookie = http.cookiejar.CookieJar()
        self.handler = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.handler)
        urllib2.install_opener(self.opener)


    def sign(self,data):
        global a
        headers = {
            'Host': 'm.client.10010.com',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Cookie': 'channel=GGPD; city=034|358; devicedId=FE0172BD-1BF5-4774-BC31-DD77360C3214; c_sfbm=234g_00; logHostIP=null; mobileService1=1Y4RfyPLLL0tvLpGnRK2QL5gQg1bDWSjnLvZ2RWKtWBWYywxWQpL!899433259; mobileServiceAll=dfd8b2e9f03c6c97f078fed5a9b73a86',
            'User-Agent': 'ChinaUnicom4.x/230 CFNetwork/1128.0.1 Darwin/19.6.0',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Length': '910'
        }
        data = data.encode('utf-8')
        req2 = urllib2.Request("http://m.client.10010.com/mobileService/login.htm",headers=headers)
        req2 = urllib2.urlopen(req2,data)
        if req2.getcode() == 200:
            print('login success!')
        try:
            for item1 in self.cookie:
                if item1.name == 'a_token':
                    a = item1.value
        except:
            print("cant get cookies")
        data2={'stepflag':'22'}
        data2=urllib.parse.urlencode(data2).encode('utf-8')
        
        req3 = urllib2.Request("https://act.10010.com/SigninApp/signin/querySigninActivity.htm?token=" + a)
        if urllib2.urlopen(req3).getcode() == 200:
            print('querySigninActivity success!')
        
        req4 = urllib2.Request("https://act.10010.com/SigninApp/signin/daySign", "btnPouplePost".encode('utf-8'))
        if urllib2.urlopen(req4).getcode() == 200:
            print('daySign success!')
            
        req5 = urllib2.Request("https://act.10010.com/SigninApp/signin/getIntegral")
        r = self.opener.open(req5)
        print( ' coin: ' + r.read().decode('utf-8'))
        
        data2={'stepflag':'22'}
        data2=urllib.parse.urlencode(data2).encode('utf-8')
        data3={'stepflag':'23'}
        data3=urllib.parse.urlencode(data3).encode('utf-8')
        for x in range(3):
           get_req6 = urllib2.Request("http://act.10010.com/SigninApp/mySignin/addFlow",data2)
           req6 = self.opener.open(get_req6)
           get_req7 = urllib2.Request("http://act.10010.com/SigninApp/mySignin/addFlow",data3)
           req7 = self.opener.open(get_req7)
if __name__ == '__main__':

    user = Qiandao()

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = timestamp+"这部分自己按要求抓包提取"

    user.sign(data)

