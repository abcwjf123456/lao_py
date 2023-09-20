from django.test import TestCase
from multiprocessing import Process
import time


def kk(gg):
    print("%s dd" % gg)
    time.sleep(2)
    print('kkl')


# if __name__ == '__main__':
#     p = Process(target=kk, args=('kk',))
#     p.start()
#     print('z')


# Create your tests here.
class MyProcess(Process):
    def run(self):
        print("dd")
        time.sleep(2)
        print('kkl')


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print('k')
