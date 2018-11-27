# coding=utf-8
'''
@Time    : 2018/11/25 12:03
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 80_Remove_Duplicates_from_Sorted_Array_II.py
@Software: PyCharm
'''


class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
    #         return len(nums)
    #     flag = 0
    #     while flag == 0:
    #         for i in range(len(nums)):
    #             if nums.count(nums[i]) > 2:
    #                 nums.pop(i)
    #                 break
    #             if i == len(nums)-1:
    #                 flag = 1
    #     return len(nums)

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0

        for i in range(len(nums)):
            pass



if __name__ == '__main__':
    a = Solution()
    print a.removeDuplicates([1,1,1,2,2,3])
