#coding=utf-8
'''
@Time    : 2018/10/29 08:48
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : Graph_maxtrix.py
@Software: PyCharm
'''

class Graph(object):
    '''
    图的邻接矩阵表示
    '''
    def __init__(self, mat, unconn=0):
        '''
        初始化
        :param mat: 二维表参数
        :param unconn:
        '''
        vnum = len(mat)

        # 每一行的数据是否一致, 方形
        for x in mat:
            if len(x) != vnum:
                return

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
        return False

    def add_edge(self, vi, vj, val=1):
        '''
        增加边
        :param vi:
        :param vj:
        :param val:
        :return:
        '''
        return False

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
        return self._mat[vi][vj]

    def __call__(self, *args, **kwargs):
        print 'Graph'

g = Graph([[1, 3], [2, 3]])
print g.__dict__
#print g.__class__
