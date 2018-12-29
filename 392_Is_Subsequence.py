#coding=utf-8
'''
@Time    : 2018/12/24 22:13
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 392_Is_Subsequence.py
@Software: PyCharm
'''


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        index = 0
        for i in range(len(t)):
            if t[i] == s[index]:
                index += 1
                if index == len(s)-1:
                    return True
        return False

