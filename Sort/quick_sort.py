# coding=utf-8
from collections import deque


class Solution(object):

    # 挖坑填数+分治法
    def quick(self, nums, left, right):
        i = left
        j = right
        std = nums[i]
        while i < j:
            while i < j and nums[i] < std:
                i += 1
        pass

    def select(self, nums):
        for i in range(len(nums)):
            min = nums[i]
            index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < min:
                    min = nums[j]
                    index = j
            nums[i], nums[index] = nums[index], nums[i]
        return nums


if __name__ == '__main__':
    a = Solution()
    b = [2, 3, 1, 4, 5]
    print a.select(b)
