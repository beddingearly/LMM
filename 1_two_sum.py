#coding=utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result
    def fake_bubble_sort(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
        return nums
    def real_bubble_sort(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = tmp
            print nums
        return nums



if __name__ == '__main__':
    nums = [2, 11, 7, 15, 13, 6, 4, 8, -1, 34, 22]
    target = 9
    a = Solution()
    print a.twoSum(nums, target)
    #print a.fake_bubble_sort(nums)
    #print a.real_bubble_sort(nums)