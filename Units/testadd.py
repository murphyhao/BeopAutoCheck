#coding=utf-8

import unittest
from common import CCaseCage
from Tools.calculator import Count


class TestAdd(CCaseCage):

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)


if __name__ == '__main__':
    unittest.main()
