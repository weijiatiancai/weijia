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
        print "行业管理接口自动化开始测试"
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

    def test_a_product_add(self):
        u'''新增行业'''
        #新建行业+节点
        print "新建行业接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/'  # 真正的接口url
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        data={"summary":"fidder3",
              "name":"fidder4",
              "newHotStatus":2,
              "file1":"1.png",
              "file2":"1.png",
              "isRedPointBottom":1,
              "picSmall":"08/29/03/Ie3R2o.png",
              "picMiddle":"08/29/03/bd9dct.png",
              "hyspNewHotStatus":0,
              "insightNewHotStatus":0,
              "jjclNewHotStatus":0,
              "jjfaNewHotStatus":0,
              "cptjNewHotStatus":0,
              "sclNewHotStatus":0,
              "hyalNewHotStatus":0,
              "textContent":"123",
              "hyalDatagridList":'[{"page":1,"rows":10,"sort":null,"order":null,"pager":{"pageId":1,"rowCount":0,"pageSize":10,"pageCount":0,"pageOffset":0,"pageTail":0,"orderField":"","orderDirection":true,"length":6,"startIndex":1,"endIndex":0,"indexs":[],"orderCondition":"","mysqlQueryCondition":" limit 0,10","oracleQueryCondition":null},"id":20,"title":"云视讯宣传单页","filename":"云视讯宣传单页","status":1,"path":"20/20/","file":"20.pdf","type":1,"size":10577417,"pages":2,"imgStatus":2,"creater":1,"createrName":"系统管理员","createDate":"2016-06-07 10:46:54","updater":1,"updaterName":"系统管理员","updateDate":"2017-08-04 09:16:47","remark":"产品云视讯宣传材料","seq":null,"companyId":1,"companyName":"政企分公司","newHotStatus":0}]',
              "jjfaDatagridList":'[{"page":1,"rows":10,"sort":null,"order":null,"pager":{"pageId":1,"rowCount":0,"pageSize":10,"pageCount":0,"pageOffset":0,"pageTail":0,"orderField":"","orderDirection":true,"length":6,"startIndex":1,"endIndex":0,"indexs":[],"orderCondition":"","mysqlQueryCondition":" limit 0,10","oracleQueryCondition":null},"id":20,"title":"云视讯宣传单页","filename":"云视讯宣传单页","status":1,"path":"20/20/","file":"20.pdf","type":1,"size":10577417,"pages":2,"imgStatus":2,"creater":1,"createrName":"系统管理员","createDate":"2016-06-07 10:46:54","updater":1,"updaterName":"系统管理员","updateDate":"2017-08-04 09:16:47","remark":"产品云视讯宣传材料","seq":null,"companyId":1,"companyName":"政企分公司","newHotStatus":0}]',
              "hyspDatagridList":'[{"id":2285,"hostLogo":"08/25/04/JHjG2q.png","hostId":22,"hostName":"海南公司","name":"视频文件1","intro":"","duration":"00:00:12","url":"08/25/04/CrsNnz.mp4","appCoverSmall":"08/25/04/3DgIdh.jpg","pcCoverSmall":"08/25/04/6JVe8P.jpg","appCover":"http://223.105.4.162:9083/testshare/08/25/04/3DgIdh.jpg","pcCover":"08/25/04/XjmgAd.jpg","hostInfo":"苏研中心","startTime":null,"endTime":null,"type":"44","status":2,"createTime":"2017-08-25 16:51:00","updateTime":"2017-08-25 16:51:07","creater":1,"updater":1,"size":"4795","seq":null,"newHotStatus":0,"createbyStr":null,"updatebyStr":null}]'

        }
        K3 = self.s.post(url=r, json=data, headers=headers)  # 发送请求
        print K3.text
        print "code:" + str(K3.status_code)


    def test_b_Industry_inquire(self):
        u'''行业列表查询'''
        # 行业列表查询
        print'行业列表查询接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry'
        data = {"page": 1, "rows": 10}
        K3 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        print K3.text
        print "code:" + str(K3.status_code)
        num = re.findall('"id":(\d+)', K3.text)[0]
        #print num
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K3.text)
        self.assertIn("000000", K3.text)


    def test_c_Industry_revise(self):
        u'''修改行业'''
        # 先行业列表查询
        data = {"page": 1, "rows": 10}
        K2=self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)

        #再修改行业
        print"修改行业接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/'  # 真正的接口url
        headers = {"Content-Type": "application/json"
                   # 'Accept':'application/json, text/plain, */*'
                   }
        data = {"id":num,
                "summary": "自动化测试",
                "name": "测试工程师",
                "newHotStatus": 2,
                "file1": "1.png",
                "file2": "1.png",
                "isRedPointBottom": 1,
                "picSmall": "08/29/03/Ie3R2o.png",
                "picMiddle": "08/29/03/bd9dct.png",
                "hyspNewHotStatus": 0,
                "jjfaNewHotStatus": 0,
                "hyalNewHotStatus": 0,
                "cptjNewHotStatus": 0,
                "insightNewHotStatus": 2,
                "jjclNewHotStatus": 2,
                "sclNewHotStatus": 2,
                "textContent": "1234567890",
                "hyspDatagridList": '[{"id":2285,"name":"视频文件1","type":"44","seq":null,"newHotStatus":1,"nodeLevel2NewHotStatus":0,"nodeLevel2Type":"31"}]',
                "jjfaDatagridList": '[{"id":20,"title":"云视讯宣传单页","seq":null,"newHotStatus":2,"nodeLevel2NewHotStatus":0,"nodeLevel2Type":"2004"}]',
                "hyalDatagridList": '[{"id":20,"title":"云视讯宣传单页","seq":null,"newHotStatus":2,"nodeLevel2NewHotStatus":0,"nodeLevel2Type":"2005"}]',
                "cptjDatagridList":'[{"id":45863,"name":"没产品介绍","seq":null,"nodeLevel2NewHotStatus":0,"nodeLevel2Type":"28","newHotStatus":0}]',
                "insightDatagridList":'[{"id":20,"title":"云视讯宣传单页","seq":null,"newHotStatus":1,"nodeLevel2NewHotStatus":2,"nodeLevel2Type":"2006"}]',
                "jjclDatagridList":'[{"id":20,"title":"云视讯宣传单页","seq":null,"newHotStatus":0,"nodeLevel2NewHotStatus":2,"nodeLevel2Type":"2007"}]',
                "sclDatagridList":'[{"id":20,"title":"云视讯宣传单页","seq":null,"newHotStatus":2,"nodeLevel2NewHotStatus":2,"nodeLevel2Type":"2011"}]'
                }
        K4 = self.s.put(url=r, json=data, headers=headers)  # 发送请求
        print K4.text
        print "code:" + str(K4.status_code)
        self.assertIn("000000", K4.text)


    def test_d_Industrys_ViewDetails(self):
        u'''进入行业详情'''
        # 行业列表查询
        data = {"page": 1, "rows": 10}
        K2=self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)

        # 进入行业详情
        print "进入行业详情接口--http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/"
        P = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/'
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



    def test_e_Industrys_Get(self):
        u'''行业下线'''
        # 行业列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        # status= re.findall('"status":(\d+)', K2.text)[0]
        # print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        #print K2.text
        #print K2.status_code

        print "动态编辑-下线--http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/op"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/op'
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
        # 行业列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        #print K2.text
        #print K2.status_code
        # num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        #print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        assert "3" in status
        self.assertIn('"status":3', K2.text)

    def test_f_Industrys_up(self):
        u'''行业上线'''
        # 行业列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        # status= re.findall('"status":(\d+)', K2.text)[0]
        # print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        #print K2.text
        #print K2.status_code

        print "动态编辑-上线--http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/op"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/op'
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
        # 行业列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        #print K2.text
        #print K2.status_code
        # num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        #print status
        #num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        assert "2" in status
        self.assertIn('"status":2', K2.text)



    def test_g_Industrys_updata(self):
        u'''行业同步数据'''
        # 行业列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        # status= re.findall('"status":(\d+)', K2.text)[0]
        # print status
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        #print K2.text
        #print K2.status_code

        print "行业编辑-同步数据--http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/op"
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/op'
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
        #self.assertIn('"status":2', K2.text)

        # 断言需要
        # 行业列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        #print K2.text
        #print K2.status_code
        # num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status = re.findall('"status":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        assert "2" in status
        self.assertIn('"status":2', K2.text)


    def test_h_Industrys_GetDelete(self):
        u'''上线状态删除'''
        # 先行业详情查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)

        #再行业动态
        print'上线状态删除行业接口--http://223.105.4.162:9082/psp-management/industry/delete.do'
        data = {"id": num}
        r = 'http://223.105.4.162:9082/psp-management/industry/delete.do'
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
        #self.assertIn("只有编辑状态与下线状态才能删除!", K2.text)





    def test_i_Industrys_UpDelete(self):
        u'''下线状态删除'''
        # 行业列表查询
        data = {"page": 1, "rows": 10}
        K2 = self.s.get('http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry', params=data)
        num = re.findall('"id":(\d+)', K2.text)[0]
        # 获取返回数据第一个status
        status= re.findall('"status":(\d+)', K2.text)[0]
        # num = re.findall('"data":(.*?)\}', aa)[0]
        self.assertIn("sequenceNumber", K2.text)
        #print K2.text
        #print K2.status_code

        #先行业下线
        r = 'http://223.105.4.162:9082/psp-management/v1/admin/cmssIndustry/op'
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
        #print K4.text
        #print K4.status_code
        # self.assertIn('"status":9', K2.text)

        print'下线状态删除行业接口--http://223.105.4.162:9082/psp-management/industry/delete.do'
        data = {"id": num}
        r = 'http://223.105.4.162:9082/psp-management/industry/delete.do'
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
