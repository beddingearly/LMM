#coding=utf-8
'''
@Time    : 2018/12/24 20:48
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 665_Non-decreasing_Array.py
@Software: PyCharm
'''



class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cot = 0
        index = 0
        for i in range(1, len(nums) - 1, 1):
            if i == 0:
                if nums[i] > nums[i+1]:
                    index = i
                cot += 1
            elif nums[i] > nums[i+1]:
                if nums[i-1] >= nums[i+1]:
                    index = i+1
                else:
                    index = i
                cot += 1
        print cot
        print index
        print nums
        if cot == 0:
            return True
        elif cot == 1:
            nums.pop(index)
            print nums
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    return False
            return True
        else:
            return False