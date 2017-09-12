# coding=utf-8
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
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print "产品管理接口自动化开始测试"
        print"请等待------------------"
        # 登录login
        self.s = requests.Session()
        self.s.auth = ('user', 'pass')
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/entrys/login'  # 真正的接口url
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        data = {"email": "admin@qq.com", "pwd": "1234567890"}

        self.s.post(url=r, data=json.dumps(data), headers=headers)  # 发送请求

    def test_a_Product_add(self):
        u'''新增产品'''
        # 新建产品+节点
        print "新建产品接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/'  # 真正的接口url
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        data = {"summary": "fidder3",
                "name": "fidder4",
                "newHotStatus": 3,
                "file1": "1.png",
                "file4": "1.png",
                "other2" :1,
                "isRedPointBottom": 1,
                "picSmall": "08/29/03/Ie3R2o.png",
                "picMiddle": "08/29/03/bd9dct.png",
                "textContent": "测试测试测试",
                "classificationId":1002,
                "cpspNewHotStatus": 0,
                "xcclNewHotStatus": 0,
                "pxclNewHotStatus": 0,
                "dxalNewHotStatus": 0,
                "sclNewHotStatus": 0,
                "jjclNewHotStatus": 0,
                "lxxxNewHotStatus": 0,
                "cpspDatagridList": '[{"id":2262,"hostLogo":"07/30/04/TpmvVe.png","hostId":1,"hostName":"政企分公司","name":"测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播","intro":"测试一下测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测","duration":"","url":"https://www.douyu.com/1867637","appCoverSmall":"07/30/04/gyFYbZ.png","pcCoverSmall":"07/30/04/o8p8Hn.png","appCover":"http://223.105.4.162:9083/testshare/07/30/04/gyFYbZ.png","pcCover":"07/30/04/o8p8Hn.png","hostInfo":"测试文字信息测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播","startTime":"2017-08-14 18:55:00","endTime":"2017-08-15 22:55:00","type":"55","status":2,"createTime":"2017-07-30 16:55:35","updateTime":"2017-08-25 15:41:53","creater":1,"updater":1,"size":null,"seq":null,"newHotStatus":0,"createbyStr":null,"updatebyStr":null}]',
                "xcclDatagridList": '[{"page":1,"rows":10,"sort":null,"order":null,"pager":{"pageId":1,"rowCount":0,"pageSize":10,"pageCount":0,"pageOffset":0,"pageTail":0,"orderField":"","orderDirection":true,"length":6,"startIndex":1,"endIndex":0,"indexs":[],"orderCondition":"","mysqlQueryCondition":" limit 0,10","oracleQueryCondition":null},"id":20,"title":"云视讯宣传单页","filename":"云视讯宣传单页","status":1,"path":"20/20/","file":"20.pdf","type":1,"size":10577417,"pages":2,"imgStatus":2,"creater":1,"createrName":"系统管理员","createDate":"2016-06-07 10:46:54","updater":1,"updaterName":"系统管理员","updateDate":"2017-08-04 09:16:47","remark":"产品云视讯宣传材料","seq":null,"companyId":1,"companyName":"政企分公司","newHotStatus":0}]'
                }
        K3 = self.s.post(url=r, json=data, headers=headers)  # 发送请求
        print K3.text
        print "code:" + str(K3.status_code)

    def test_b_Product_inquire(self):
        u'''产品列表查询'''
        # 产品列表查询
        print'产品列表查询接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct'
        data = {"page": 1, "rows": 10}
        K3 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        print K3.text
        print "code:" + str(K3.status_code)
        num = re.findall('"id":(\d+)', K3.text)[0]
        # print num
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K3.text)
        self.assertIn("000000", K3.text)

    def test_c_Product_revise(self):
        u'''修改产品'''
        # 先产品列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)

        # 再修改产品
        print"修改产品接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/'  # 真正的接口url
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        data = {"id":num,
                "summary": "fidder4",
                "name": "fidder4",
                "newHotStatus": 3,
                "file1": "1.png",
                "file4": "1.png",
                "other2": 1,
                "isRedPointBottom": 1,
                "picSmall": "08/29/03/Ie3R2o.png",
                "picMiddle": "08/29/03/bd9dct.png",
                "textContent": "测试测试测试呼呼哈",
                "classificationId": 1002,
                "cpspNewHotStatus": 0,
                "xcclNewHotStatus": 0,
                "pxclNewHotStatus": 0,
                "dxalNewHotStatus": 0,
                "sclNewHotStatus": 0,
                "jjclNewHotStatus": 0,
                "lxxxNewHotStatus": 0,
                "cpspDatagridList": '[{"id":2262,"hostLogo":"07/30/04/TpmvVe.png","hostId":1,"hostName":"政企分公司","name":"测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播","intro":"测试一下测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗测试斗鱼直播测","duration":"","url":"https://www.douyu.com/1867637","appCoverSmall":"07/30/04/gyFYbZ.png","pcCoverSmall":"07/30/04/o8p8Hn.png","appCover":"http://223.105.4.162:9083/testshare/07/30/04/gyFYbZ.png","pcCover":"07/30/04/o8p8Hn.png","hostInfo":"测试文字信息测试斗鱼直播测试斗鱼直播测试斗鱼直播测试斗鱼直播","startTime":"2017-08-14 18:55:00","endTime":"2017-08-15 22:55:00","type":"55","status":2,"createTime":"2017-07-30 16:55:35","updateTime":"2017-08-25 15:41:53","creater":1,"updater":1,"size":null,"seq":null,"newHotStatus":0,"createbyStr":null,"updatebyStr":null}]',
                "xcclDatagridList": '[{"page":1,"rows":10,"sort":null,"order":null,"pager":{"pageId":1,"rowCount":0,"pageSize":10,"pageCount":0,"pageOffset":0,"pageTail":0,"orderField":"","orderDirection":true,"length":6,"startIndex":1,"endIndex":0,"indexs":[],"orderCondition":"","mysqlQueryCondition":" limit 0,10","oracleQueryCondition":null},"id":20,"title":"云视讯宣传单页","filename":"云视讯宣传单页","status":1,"path":"20/20/","file":"20.pdf","type":1,"size":10577417,"pages":2,"imgStatus":2,"creater":1,"createrName":"系统管理员","createDate":"2016-06-07 10:46:54","updater":1,"updaterName":"系统管理员","updateDate":"2017-08-04 09:16:47","remark":"产品云视讯宣传材料","seq":null,"companyId":1,"companyName":"政企分公司","newHotStatus":0}]'
                }
        K4 = self.s.put(url=r, json=data, headers=headers)  # 发送请求
        print K4.text
        print "code:" + str(K4.status_code)
        self.assertIn("000000", K4.text)

    def test_d_Products_ViewDetails(self):
        u'''进入产品详情'''
        # 产品列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)

        # 进入产品详情
        print "进入产品详情接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct"
        P = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/'
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
        self.assertIn("SUCCESS", K5.text)

    def test_e_Product_Get(self):
        u'''产品下线'''
        # 产品列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        # status= re.findall('"status":(\d+)', K2.text)[0]
        # print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        # print K2.text
        # print K2.status_code

        print "产品编辑-下线--http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/op"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/op'
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
        # self.assertIn('"status":9', K2.text)

        # 断言需要
        # 产品列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        # print K2.text
        # print K2.status_code
        # num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        # print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        assert "3" in status
        self.assertIn('"status":3', K2.text)

    def test_f_Products_up(self):
        u'''产品上线'''
        # 产品列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        # status= re.findall('"status":(\d+)', K2.text)[0]
        # print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        # print K2.text
        # print K2.status_code

        print "产品编辑-上线--http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/op"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/op'
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
        # self.assertIn('"status":9', K2.text)

        # 断言需要
        # 产品列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        # print K2.text
        # print K2.status_code
        # num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        # print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        assert "2" in status
        self.assertIn('"status":2', K2.text)

    def test_g_Products_updata(self):
        u'''产品同步数据'''
        # 产品列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        # status= re.findall('"status":(\d+)', K2.text)[0]
        # print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        # print K2.text
        # print K2.status_code

        print "产品编辑-同步数据--http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/op"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/op'
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
        # self.assertIn('"status":2', K2.text)

        # 断言需要
        # 产品列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        # print K2.text
        # print K2.status_code
        # num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        assert "2" in status
        self.assertIn('"status":2', K2.text)

    def test_h_Products_GetDelete(self):
        u'''上线状态删除'''
        # 先产品详情查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)

        # 再删除产品
        print'上线状态删除产品接口--http://223.105.4.162:9082/psp-management/product/delete.do'
        data = {"id": num}
        r = 'http://223.105.4.162:9082/psp-management/product/delete.do'
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
        # self.assertIn("只有编辑状态与下线状态才能删除!", K2.text)

    def test_i_Products_UpDelete(self):
        u'''下线状态删除'''
        # 产品列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        # print K2.text
        # print K2.status_code

        # 先产品下线
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssProduct/op'
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
        # print K4.text
        # print K4.status_code
        # self.assertIn('"status":9', K2.text)

        print'下线状态删除行业接口--http://223.105.4.162:9082/psp-management/product/delete.do'
        data = {"id": num}
        r = 'http://223.105.4.162:9082/psp-management/product/delete.do'
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
        print"测试结束---end"
        pass


if __name__ == '__main__':
    unittest.main()
