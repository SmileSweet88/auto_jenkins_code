import time
import unittest

from BeautifulReport import BeautifulReport
import logging

from HTMLTestRunner import HTMLTestRunner

from case.test_ihrm_employ import TestIhrmEmpoly
from case.test_ihrm_login import TestIhrmLogin
from constant.constant import workPath, log_config

log_config()

suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(TestIhrmLogin))
suit.addTest(unittest.makeSuite(TestIhrmEmpoly))
# fileName = "{}ihrm_employ.html".format(time.strftime("%Y%m%d%H%M%S"))
# fileName = "report.html"
# filePath = workPath + "/report/"
report_path = "./report/report.html"
with open(report_path, "wb") as f:
    # 实例化HTMLTestRunner对象，传入报告文件流f
    runner = HTMLTestRunner(stream=f, title="test_Hr_employ", description="test_my")
runner.run(suit)
# BeautifulReport(suit).report(filename=fileName, description="hello", log_path=filePath)
