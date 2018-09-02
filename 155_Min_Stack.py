class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.s == []:
            return
        return self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.s == []:
            return
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.s == []:
            return
        return min(self.s)


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print obj.pop()
    print obj.top()
    print obj.getMin()
