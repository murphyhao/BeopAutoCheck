#coding=utf-8

import unittest
from common import CCaseCage
from Tools.calculator import Count


class TestOdd(CCaseCage):

    def test_odd(self):
        j = Count(1, 3)
        self.assertEqual(j.add(), 4)


if __name__ == '__main__':
    unittest.main()