# coding=utf-8
'''
@Time    : 2018/11/27 12:36
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 151_Reverse_Words_in_a_String.py
@Software: PyCharm
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.strip().split(" ")
        a.reverse()
        while '' in a:
            a.remove('')
        return " ".join(a).strip()

if __name__ == '__main__':
    a = Solution()
    print a.reverseWords("   a   b ")