#coding=utf-8
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = list(str(x))
        result1 = ''.join(a)
        a.reverse()
        result2 = ''.join(a)
        if result1 == result2:
            return True
        else:
            return False

if __name__ == '__main__':
    a = Solution()
    print a.isPalindrome(0)