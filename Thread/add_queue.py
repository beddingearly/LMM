# coding=utf-8
'''
@Time    : 2019/1/22 10:33
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : add_queue.py
@Software: PyCharm
'''
import threading
from queue import Queue
import random


def thread_job(l, q):
    q.put(l)


def multiThread():
    data = [1, 2, 3, 4]
    result = []
    q = Queue()
    threads = []
    for i in range(4):
        thread = threading.Thread(target=thread_job, args=(data[i], q))
        thread.start()
        thread.join()
        threads.append(thread)
    for _ in range(4):
        result.append(q.get())
    print result


def test():
    data = ['I', 'Love', 'You', 'Too']
    # 多线程不能直接返回数值
    # 通过中间容器保存
    # return data[random.randint(0, 3)]
    o.append(data[random.randint(0, 3)])


def test_main():
    for _ in range(4):
        t = threading.Thread(target=test)
        t.start()


if __name__ == '__main__':
    # multiThread()
    o = []
    test_main()
    print o
