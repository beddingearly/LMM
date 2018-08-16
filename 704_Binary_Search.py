# coding=utf-8
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif target not in nums:
            return -1
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return (low + high) / 2


if __name__ == '__main__':
    nums = [5]
    target = 5
    a = Solution()
    print a.search(nums=[-1, 0, 3, 5, 9, 12], target=9)
