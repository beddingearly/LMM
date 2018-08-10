# coding=utf-8
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = nums[0]
        for i in range(1, len(nums)):
            if maxnum + nums[i] < maxnum:
                nums[i] = maxnum
            else:
                maxnum += nums[1]
        return maxnum
if __name__ == '__main__':
    a = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print a.maxSubArray(nums)