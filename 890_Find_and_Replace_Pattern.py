#coding=utf-8
'''
@Time    : 2018/11/30 22:03
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 890_Find_and_Replace_Pattern.py
@Software: PyCharm
'''


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        pattern = self.transfor(pattern)
        for i in words:
            j = self.transfor(i)
            if j == pattern:
                result.append(i)
        return result

    def transfor(self, pattern):
        m = {}
        j = 0
        s = "0"
        m[pattern[0]] = '0'
        for i in range(1, len(pattern), 1):
            if pattern[i-1] != pattern[i]:
                if m.has_key(pattern[i]):
                    s += m[pattern[i]]
                else:
                    j += 1
                    m[pattern[i]] = str(j)
                    s += str(j)
        return s

