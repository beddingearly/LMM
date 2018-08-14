# coding=utf-8
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1, 2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(2, n):
                result.append(result[i - 1] + result[i - 2])
        return result[n - 1]
