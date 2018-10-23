#coding=utf-8
'''
@Time    : 2018/10/20 10:40
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : Tree.py
@Software: PyCharm
'''
class TreeList(object):
    def __init__(self, data, left=None, right=None):
        self.node = [data, left, right]

    def is_empty(self):
        if len(self.btree) == 0:
            return True
        return False

    def setLeft(self, left):
        self.node[1] = left

    def setRight(self, right):
        self.node[2] = right

    def setRoot(self, root):
        self.node[0] = root

# 基于List的优先队列
class PrioQue(object):
    def __init__(self, elist=[]):
        self._elem = list(elist)
        self._elem.sort(reverse=True)

    def enqueue(self, e):
        i = 0
        while i < len(self._elem):
            if e < self._elem[i]:
                i += 1
            else:
                break
        self._elem.insert(i, e)

    def dequeue(self):
        if len(self._elem) == 0:
            return False
        return self._elem.pop()

    def is_empty(self):
        if len(self._elem) == 0:
            return True
        return False

    def top(self):
        if len(self._elem) == 0:
            return False
        return self._elem[-1]

class PriQue(object):
    '''
    Base on heap
    '''

    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        if len(self._elems) == 0:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self._elems[0]

    # 入队 向上筛选
    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)

    def dequeue(self):
        pass

    def siftdown(self):
        pass

    def buildheap(self):
        pass

    def siftup(self, e, last):
        pass

if __name__ == '__main__':
    # a = TreeList(3)
    # a.setLeft(TreeList(4, 3, 6).node)
    # print a.node
    b = PrioQue([4,3,2,1])
    b.dequeue()
    b.dequeue()
    b.dequeue()
    print b.is_empty()
    b.dequeue()
    print b.is_empty()
    print b._elem
