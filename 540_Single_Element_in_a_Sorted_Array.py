#coding=utf-8
'''
@Time    : 2018/12/26 20:00
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 540_Single_Element_in_a_Sorted_Array.py
@Software: PyCharm
'''


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cot = 1
        pre = nums[0]
        for i in range(1, len(nums), 1):
            if nums[i] == pre:
                cot += 1
            else:
                if cot == 1:
                    return pre
                else:
                    pre = nums[i]
                    cot = 1
        return nums[-1]