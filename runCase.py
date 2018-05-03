#coding=utf-8

import threading
import time
import unittest

g_strCheckDir = "./Units/"


class CMyThread(threading.Thread):
    def __init__(self, strName, nSleep):
        threading.Thread.__init__(self)
        self.m_strName = str(strName)
        self.m_nSleep = int(nSleep)

    def run(self):
        # 执行测试
        while True:
            discover = unittest.defaultTestLoader.discover(g_strCheckDir, pattern="test*.py")
            runner = unittest.TextTestRunner()
            runner.run(discover)
            time.sleep(self.m_nSleep)


def StartThreads():
    h1 = CMyThread("BaseThread", 1)
    h1.start()
    h1.join()
    print("Main thread end!")


if __name__ == '__main__':
    StartThreads()