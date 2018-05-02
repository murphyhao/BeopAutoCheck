#coding=utf-8

import threading
import time
import unittest

g_strCheckDir = "./Units/"
g_discover = unittest.defaultTestLoader.discover(g_strCheckDir, pattern="test*.py")


class CMyThread(threading.Thread):
    def __init__(self, strName, nSleep):
        threading.Thread.__init__(self)
        self.m_strName = str(strName)
        self.m_nSleep = int(nSleep)

    def run(self):
        # 执行测试
        runner = unittest.TextTestRunner()
        runner.run(g_discover)


def StartThreads():
    h1 = CMyThread("BaseThread", 1)
    h1.start()
    h1.join()
    print("Main thread end!")


if __name__ == '__main__':
    StartThreads()