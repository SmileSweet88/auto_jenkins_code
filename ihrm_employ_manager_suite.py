# encoding = utf-8
import os

import unittest
import HTMLTestRunner
from BeautifulReport import BeautifulReport

from case.test_ihrm_employ import TestIhrmEmpoly
from case.test_ihrm_login import TestIhrmLogin
from constant.constant import workPath

suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(TestIhrmLogin))
suit.addTest(unittest.makeSuite(TestIhrmEmpoly))
filePath = workPath + "/report"
BeautifulReport(suit).report(filename="report.html",log_path=filePath,description="test_employ")

# path1 = os.path.dirname(os.path.abspath(__file__))

# with open(path1 + '/report/report.html', 'wb') as f:
#     runner = HTMLTestRunner.HTMLTestRunner(f, title='text1', description='zzz')
#     runner.run(suit)
