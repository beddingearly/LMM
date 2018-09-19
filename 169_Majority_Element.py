# coding=utf-8
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 通过排序之后的数组，中间值肯定为众数
        n = len(nums) / 2
        nums.sort()
        return nums[n]
