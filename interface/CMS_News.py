#coding=utf-8
import sys
import requests
import json
from time import sleep
import unittest
import urllib2
import urllib
import cookielib
import os
import threading
import time
import HTMLTestRunner
from cookielib import CookieJar
import  re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print "动态管理接口自动化开始测试"
        print"请等待------------------"
        #登录login
        self.s = requests.Session()
        self.s.auth = ('user', 'pass')
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/entrys/login'  # 真正的接口url
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        data = {"email": "admin@qq.com", "pwd": "1234567890"}

        self.s.post(url=r, data=json.dumps(data), headers=headers)  # 发送请求

    def test_a_News_login(self):
        u'''登录首页----账号：admin@qq.com 密码：1234567890 '''
        print"登录接口--http://223.105.4.162:9082/psp-management/v1/admin/entrys/login"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/entrys/login'  # 真正的接口url
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        data = {"email": "admin@qq.com", "pwd": "1234567890"}

        K = self.s.post(url=r, data=json.dumps(data), headers=headers)  # 发送请求
        # return r.json
        print (K.text)  # 获取响应报文
        print "code:"+str(K.status_code)
        self.assertIn("000000", K.text)


    def test_b_News_add(self):
        u'''新增动态'''
        #动态详情新增
        print'新增动态接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails'
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails'  # 真正的接口url
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        data = {"name":"接口自动化测试","newHotStatus":1,"bussDate":1436933467000,"other3":"政企分公司","summary":"测试","summary2":"测试","picSmall":"06/22/07/1lyzre.jpg","textContent":"123"}

        K2=self.s.post(url=r, json=data, headers=headers)  # 发送请求
        print K2.text
        print "code:" + str(K2.status_code)
        self.assertIn("000000", K2.text)

    def test_c_News_inquire(self):
        u'''查询动态列表'''
        # 动态列表查询
        print'动态列表查询接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails'
        data = {"page": 1, "rows": 10}
        K3 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        print K3.text
        print "code:" + str(K3.status_code)
        num = re.findall('"id":(\d+)', K3.text)[0]
        #print num
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K3.text)
        self.assertIn("000000", K3.text)

    def test_d_News_revise(self):
        u'''修改动态'''
        # 先动态列表查询
        data = {"page": 1, "rows": 10}
        K2=self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)

        #再修改动态
        print"修改动态接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails'  # 真正的接口url
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        data = {"name": "测试2", "newHotStatus": 1, "bussDate": 1436933467000, "other3": "政企分公司", "summary": "测试",
                "summary2": "测试", "picSmall": "06/22/07/1lyzre.jpg", "textContent": "123","id":num}

        K4 = self.s.put(url=r, json=data, headers=headers)  # 发送请求
        print K4.text
        print "code:" + str(K4.status_code)
        self.assertIn("000000", K4.text)
    '''
    def test_trends_chaxun(self):
        # 动态列表查询
        print'查询动态列表接口'
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        print K2.text
        print K2.status_code
        num = re.findall('"id":(\d+)', K2.text)[0]
        print num
        # num = re.findall('"data":(.*?)\}', aa)[0]
        #self.assertIn("sequenceNumber", K2.text)
    '''

    def test_e_News_ViewDetails(self):
        u'''进入动态详情'''
        # 动态列表查询
        data = {"page": 1, "rows": 10}
        K2=self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)

        # 进入动态详情
        print "进入动态详情接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails"
        P = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails/'
        r = P + str(num)
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        K5 = self.s.get(url=r, headers=headers)
        print K5.text
        print "code:" + str(K5.status_code)
        self.assertIn("bussDate", K5.text)
        self.assertIn("createtime", K5.text)
        self.assertIn("000000", K5.text)

    def test_f_News_Get(self):
        u'''动态下线'''
        # 动态列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        #print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        #print K2.text
        #print K2.status_code

        print "动态编辑-下线--http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails/op"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails/op'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json",
            # "VerificationToken": "",
            "X-Requested-With": "XMLHttpRequest",
            # 　"Referer": "",
            "Content-Length": "17",
            # "Cookie": "JSESSIONID=72DFB6B767F73EF007B1B5DD3450906E",
            "Connection": "keep-alive"
        }
        data = {"ids": [num], "status": 3}
        K4 = self.s.put(url=r, json=data, headers=headers)
        print K4.text
        print "code:" + str(K4.status_code)
        self.assertIn('"status":3', K2.text)

        # 断言需要
        # 动态列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        assert "3" in status

    def test_g_News_up(self):
        u'''动态上线'''
        # 动态列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        #print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        #print K2.text
        #print K2.status_code

        print "动态编辑-上线--http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails/op"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails/op'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json",
            # "VerificationToken": "",
            "X-Requested-With": "XMLHttpRequest",
            # 　"Referer": "",
            "Content-Length": "17",
            # "Cookie": "JSESSIONID=72DFB6B767F73EF007B1B5DD3450906E",
            "Connection": "keep-alive"
        }
        data = {"ids": [num], "status": 2}
        K4 = self.s.put(url=r, json=data, headers=headers)
        print K4.text
        print "code:" + str(K4.status_code)

        # 断言需要
        # 动态列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        assert "2" in status
        self.assertIn('"status":2', K2.text)



    def test_h_News_updata(self):
        u'''动态同步数据'''
        # 动态列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        #print K2.text
        #print "code:" + str(K2.status_code)

        print "动态编辑-同步数据--http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails/op"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails/op'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json",
            # "VerificationToken": "",
            "X-Requested-With": "XMLHttpRequest",
            # 　"Referer": "",
            "Content-Length": "17",
            # "Cookie": "JSESSIONID=72DFB6B767F73EF007B1B5DD3450906E",
            "Connection": "keep-alive"
        }
        data = {"ids": [num], "status": 9}
        K4 = self.s.put(url=r, json=data, headers=headers)
        print K4.text
        print "code:" + str(K4.status_code)
        #self.assertIn('"status":9', K2.text)

        # 断言需要
        # 动态列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        assert "2" in status


    def test_i_News_GetDelete(self):
        u'''上线状态删除'''
        # 先动态详情查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)

        #再删除动态
        print'上线状态删除动态接口--http://223.105.4.162:9082/psp-management/newsDetails/delete.do'
        data = {"id": num}
        r = 'http://223.105.4.162:9082/psp-management/newsDetails/delete.do'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # "VerificationToken": "",
            "X-Requested-With": "XMLHttpRequest",
            # 　"Referer": "",
            "Content-Length": "17",
            #"Cookie": "JSESSIONID=72DFB6B767F73EF007B1B5DD3450906E",
            "Connection": "keep-alive"
        }
        K2 = self.s.post(url=r, data=data, headers=headers)
        print K2.text
        print "code:" + str(K2.status_code)
        self.assertIn("只有编辑状态与下线状态才能删除!", K2.text)

    def test_j_News_UpDelete(self):
        u'''下线状态删除'''
        # 先动态详情查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        #先下线
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssNewsDetails/op'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json",
            # "VerificationToken": "",
            "X-Requested-With": "XMLHttpRequest",
            # 　"Referer": "",
            "Content-Length": "17",
            # "Cookie": "JSESSIONID=72DFB6B767F73EF007B1B5DD3450906E",
            "Connection": "keep-alive"
        }
        data = {"ids": [num], "status": 3}
        K4 = self.s.put(url=r, json=data, headers=headers)
        self.assertIn("000000", K4.text)

        print'下线状态删除动态接口--http://223.105.4.162:9082/psp-management/newsDetails/delete.do'
        data = {"id": num}
        r = 'http://223.105.4.162:9082/psp-management/newsDetails/delete.do'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # "VerificationToken": "",
            "X-Requested-With": "XMLHttpRequest",
            # 　"Referer": "",
            "Content-Length": "17",
            # "Cookie": "JSESSIONID=72DFB6B767F73EF007B1B5DD3450906E",
            "Connection": "keep-alive"
        }
        K2 = self.s.post(url=r, data=data, headers=headers)
        print K2.text
        print "code:" + str(K2.status_code)
        self.assertIn("success", K2.text)

    @classmethod
    def tearDownClass(self):  # 与setUp()相对
        print"测试结束----end"
        pass

if __name__ == '__main__':
    unittest.main()