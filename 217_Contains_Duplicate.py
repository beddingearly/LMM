# coding=utf-8
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = set()
        for i in nums:
            if i in d:
                return True
            else:
                d.add(i)
        return False


if __name__ == '__main__':
    a = Solution()
    print a.containsDuplicate([1, 2, 3, 1])
