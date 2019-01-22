#coding=utf-8
'''
@Time    : 2019/1/22 16:09
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : my_thread.py
@Software: PyCharm
'''
import threading
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        super(MyThread, self).__init__()
        self.name = name
        self.threadID = threadID
        self.counter = counter
        self.lock = threading.Lock()

    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        self.lock.acquire()
        print(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        self.lock.release()
if __name__ == '__main__':
    threads = []
    # 创建新线程
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)

    # 开启新线程
    thread1.start()
    thread2.start()


    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

    # 等待所有线程完成，主线程才会结束
    # join方法用于线程同步
    # 防止主线程结束以后，子线程还没有来得及执行，整个程序就退出了
    for t in threads:
        t.join()
    print ("退出主线程")