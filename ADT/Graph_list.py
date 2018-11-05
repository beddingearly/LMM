#coding=utf-8
'''
@Time    : 2018/11/5 13:59
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : Graph_list.py
@Software: PyCharm
'''


class Graph(object):
    '''
    图的邻接表表示

    (前结点)
    [1, 2, 3, 4]

    (后结点，权值)
    [(2, 1), (3, 6)]
    '''

    def __init__(self, mat, unconn=0):
        vnum = len(mat)

        self._mat = [mat[i][1] for i in range(vnum)]
        self._unconn = unconn

        # 顶点数目
        self._vnum = vnum
        '''

        self.__a = '__a' # 完全不能访问
        self._a = '_a'   # 可以，但不能提示
        self.a = '1'     # 可以
        '''

    '''
    @property装饰器
    属性仅有一个self参数
    调用时，无需括号
    '''

    @property
    def vertex_num(self):
        '''
        顶点数目
        :return:
        '''
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        '''
        增加顶点
        :return:
        '''
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        '''
        增加边
        :param vi:
        :param vj:
        :param val:
        :return:
        '''
        if self._vnum == 0:
            return False
        if self._invalid(vi) or self._invalid(vj):
            return False
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:  # 修改mat[vi][vj]的值
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:  # 原来没有到vj的边，推出循环后加入该边
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        '''

        :param vi:
        :param vj:
        :return:
        '''
        if self._invalid(vi) or self._invalid(vj):
            return False
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            return
        return self._mat[vi]

    def __call__(self, *args, **kwargs):
        print 'Graph'


g = Graph([[1, 3], [2, 3]])
print g.__dict__
# print g.__class__
