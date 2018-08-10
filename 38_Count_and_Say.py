# coding=utf-8
# 11 不读 one one one one,读 two one, 连着一起相同的数会先说数量再说值
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        elif n == 3:
            return '21'
        for i in range()