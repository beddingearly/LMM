# coding=utf-8
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        while(i != length):
            if nums[i] == val:
                nums.remove(nums[i])
                length -= 1
            else:
                i += 1
        return len(nums)

if __name__ == '__main__':
    a = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print a.removeElement(nums, val)