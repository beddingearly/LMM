#coding=utf-8
'''
@Time    : 2018/11/5 14:41
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : DFS.py
@Software: PyCharm
'''

class Stack(object):
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        return self.s.pop()

    def top(self):
        return self.s[-1]

    def is_empty(self):
        if len(self.s) == 0:
            return True
        return False


def DFS(graph, v0):
    '''
    深度遍历搜索
    :param graph:
    :param v0:
    :return:
    [[0, (2, 1)], [1, (3, 6), (4, 1)]]
    前者既是序号也是前一个点
    '''
    vnum = len(graph)
    visited = [0] * vnum
    visited[v0] = 1
    DFS_seq = []
    st = Stack()
    st.push(v0)
    while not st.is_empty():
        tmp = st.pop()
        DFS_seq.append(tmp)
        print(tmp)
        for i in graph[tmp]:
            if visited[i[0]] == 0:
                visited[i[0]] = 1
                st.push(i[0])

    return DFS_seq
if __name__ == '__main__':
    g = {0: [(1, 1), (2, 2)],
         1: [(1, 0), (2, 5)],
         2: [(0, 2), (1, 5), (4, 6), (3, 7)],
         3: [(2, 7)],
         4: [(2, 6)]}
    # g = GraphAL(gg)
    print DFS(g, 0)
