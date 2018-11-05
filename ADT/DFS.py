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
        e = self.s[0]
        self.s = self.s[1:]
        return e, self.s
    def top(self):
        return self.s[0]

    def is_empty(self):
        if len(self.s) == 0:
            return True
        return False

def DFS(graph, v0):
    vnum = graph.vertex_num()
    visited = [0] * vnum
    visited[v0] = 1
    DFS_seq = [v0]
    st = Stack()
    st.push((0, graph.out_edges(v0)))
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i + 1, edges))  # 下次访问
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0,graph.out_edges(v)))
    return DFS_seq
