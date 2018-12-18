#coding=utf-8
'''
@Time    : 2018/12/14 09:55
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 347_Top_K_Frequent_Elements.py
@Software: PyCharm
'''
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # create a dict,a val with its count
        c = Counter(nums)
        return [item[0] for item in c.most_common(k)]

