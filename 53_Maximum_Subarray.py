# coding=utf-8
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre + nums[i] > nums[i]:
                nums[i] += pre
            pre = nums[i]
        return max(nums)
if __name__ == '__main__':
    a = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print a.maxSubArray(nums)