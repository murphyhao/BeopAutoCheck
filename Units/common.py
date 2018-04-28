#coding:utf-8
import sys
import unittest

sys.path.append("../BeopAutoCheck/Tools/")


class CCaseCage(unittest.TestCase):

    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")
