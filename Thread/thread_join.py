#coding=utf-8
'''
@Time    : 2019/1/22 10:19
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : thread_join.py
@Software: PyCharm

如果没有join()，程序顺序执行，主线程直接跳过子线程执行；
 若子线程调用join方法，主线程阻塞，等待该子线程，子线程运行完再执行主线程
'''
import threading
import time
def thread_job():
    print('T1 start\n')
    for i in range(100):
        time.sleep(0.1)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    added_thread.start()
    thread2.start()

    # 激活的线程数目
    print threading.active_count()
    # 运行线程的线程名
    print threading.enumerate()
    # 当前运行的线程
    print threading.current_thread()

    thread2.join()
    added_thread.join()

    print('all done\n')

if __name__ == '__main__':
    main()