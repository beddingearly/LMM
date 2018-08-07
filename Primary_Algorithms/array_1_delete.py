class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        cot = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                cot += 1
        return cot

if __name__ == '__main__':
    a = Solution()
    nums = [1,1,2]
    print a.removeDuplicates(nums)