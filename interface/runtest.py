# coding:utf-8
import unittest
import json
import requests
from HTMLTestRunner import HTMLTestRunner
import time

# 定义测试用例的目录为当前目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='CMS*.py')

if __name__ == "__main__":
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    #filename = './' + now + 'test_result.html'
    filename = 'index.html'

    fp = open(filename, "wb")
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="产品共享平台CMS后台接口自动化测试报告-----------------------Python编写--------------------------测试：魏佳",
                            description="测试用例执行情况：行业---动态---产品")
    # 运行测试
    runner.run(discover)
    fp.close()  # 关闭报告文件