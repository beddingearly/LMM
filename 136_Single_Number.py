#coding=utf-8
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # remember % ^ /
        result = 0
        for i in nums:
            result ^= i
        return result
