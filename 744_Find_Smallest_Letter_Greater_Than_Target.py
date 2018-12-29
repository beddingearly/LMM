#coding=utf-8
'''
@Time    : 2018/12/29 14:35
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 744_Find_Smallest_Letter_Greater_Than_Target.py
@Software: PyCharm
'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for x in letters:
            if x >target:
                return x
        return letters[0]
if __name__ == '__main__':
    s = Solution()
    print s.nextGreatestLetter(["c","f","j"], "a")