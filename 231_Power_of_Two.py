# coding=utf-8
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while (n):
            if n == 1:
                return True
            elif n % 2 != 0:
                return False
            n /= 2
