#coding=utf-8

import unittest
import sys
import time

sys.path.append("../BeopAutoCheck/")


class CCaseCage(unittest.TestCase):

    def setUp(self):
        self.m_tmStart = time.time()

    def tearDown(self):
        strUseTime = time.time() - self.m_tmStart
        strUseTime = str('%.2f' % strUseTime)
        print("This case cost %s sec" % strUseTime)