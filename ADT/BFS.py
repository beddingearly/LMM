#coding=utf-8
'''
@Time    : 2018/11/5 19:41
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : BFS.py
@Software: PyCharm
'''
from collections import deque
def BFS(graph, v0):
    '''
    广度遍历搜索
    :param graph:
    :param v0:
    :return:
    '''
    vnum = len(graph)
    visited = [0] * vnum
    visited[v0] = 1
    BFS_seq = []
    qu = deque([])
    qu.append(v0)
    while not len(qu) == 0:
        tmp = qu.popleft()
        BFS_seq.append(tmp)
        for i in graph[tmp]:
            if visited[i[0]] == 0:
                visited[i[0]] = 1
                qu.append(i[0])
    return BFS_seq
if __name__ == '__main__':
    g = {0: [(1, 1), (2, 2)],
         1: [(1, 0), (2, 5)],
         2: [(0, 2), (1, 5), (4, 6), (3, 7)],
         3: [(2, 7)],
         4: [(2, 6)]}
    print BFS(g, 0)
