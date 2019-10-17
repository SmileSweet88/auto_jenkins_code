import time
import unittest

from BeautifulReport import BeautifulReport
import logging

from case.test_ihrm_employ import TestIhrmEmpoly
from case.test_ihrm_login import TestIhrmLogin
from constant.constant import workPath, log_config

log_config()
try:
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(TestIhrmLogin))
    suit.addTest(unittest.makeSuite(TestIhrmEmpoly))
    # fileName = "{}ihrm_employ.html".format(time.strftime("%Y%m%d%H%M%S"))
    fileName = "report.html"
    filePath = workPath + "/report/"
    BeautifulReport(suit).report(filename=fileName, description="hello", log_path=filePath)
except Exception as es:
    print("**************")
    logging.info(es)