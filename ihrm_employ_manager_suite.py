import os

import unittest
import HTMLTestRunner

from case.test_ihrm_employ import TestIhrmEmpoly
from case.test_ihrm_login import TestIhrmLogin

suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(TestIhrmLogin))
# suit.addTest(unittest.makeSuite(TestIhrmEmpoly))

path1 = os.path.dirname(os.path.abspath(__file__))

with open(path1 + '/report/report.html', 'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(f, title='text1', description='老子的报告')
    runner.run(suit)
