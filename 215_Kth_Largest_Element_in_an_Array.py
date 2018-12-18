#coding=utf-8
'''
@Time    : 2018/12/14 09:48
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 215_Kth_Largest_Element_in_an_Array.py
@Software: PyCharm
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]
