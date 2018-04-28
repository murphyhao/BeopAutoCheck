#coding:utf-8
import unittest
from common import CCaseCage
from calculator import Count


class TestSub(CCaseCage):

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)


if __name__ == '__main__':
    unittest.main()