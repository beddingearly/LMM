# coding=utf-8
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
if __name__ == '__main__':
    a = Solution()
    nums = [1,3,5,6]
    target = 0
    print a.searchInsert(nums, target)
