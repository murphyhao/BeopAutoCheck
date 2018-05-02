#coding=utf-8

import unittest
import sys

sys.path.append("../BeopAutoCheck/")


class CCaseCage(unittest.TestCase):

    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")
