# coding=utf-8
'''
@Time    : 2019/1/22 08:40
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : addThread.py
@Software: PyCharm
'''
import threading
import time

def thread_job():
    print 'job1 start'
    for _ in range(10):
        time.sleep(0.1)
    print "job1 finished"

def thread_job2():
    print 'job2 start'
    print 'job2 finished'

def main():
    # 增加线程，使每个线程执行特定的功能
    add_thread = threading.Thread(target=thread_job)  # 不能加括号啊
    add_thread2 = threading.Thread(target=thread_job2)
    add_thread.start()
    add_thread2.start()

    # Wait until the thread terminates.
    # 等会调用join方法的线程 主线程再结束
    add_thread2.join()
    add_thread.join()
    print 'all down'


if __name__ == '__main__':
    # 激活的线程数目
    print threading.active_count()

    # 运行线程的线程名
    print threading.enumerate()

    # 当前运行的线程
    print threading.current_thread()

    main()

    # 如果没有join()，程序顺序执行，主线程直接跳过子线程执行；
    # 若子线程调用join方法，加入到主线程中，原主线程阻塞，等待该子线程，子线程运行完再执行主线程，
    # 来防治主线程结束以后，子线程还没有来得及执行，整个程序就退出了
