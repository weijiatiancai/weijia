#coding:utf-8
import os
import unittest
import time
import HTMLTestRunner
#当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
def add_case(caseName="Case",rule="test*.py"):
    #第一步 加载所有测试用例
    case_path =os.path.join(cur_path,caseName) #用例文件夹
    #如果文件不存在就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print "test case path:%s"%case_path
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,
                                                   top_level_dir=None)
    print discover
    return discover

def run_test(all_case,reportname="report"):
    '''第二步：执行所有用例，并把结果写入HTMl测试报告'''
    now = time.strftime("%Y_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportname) #用例文件夹
    #如果不存在这个report文件夹,系统默认自动创建
    if not os.path.exists(report_path): os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now+"result.html")
    print "report path:%s"%report_abspath
    fp =open(report_abspath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"自动化测试报告",
                                           description=u"用例执行情况：")
    #调用add_case函数返回值
    runner.run(all_case)
    fp.close()