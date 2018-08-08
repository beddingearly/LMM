#coding=utf-8
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack:
            return 0
        len1 = len(needle)
        for i in range(len(haystack)-len1+1):
            target = haystack[i:i+len1]
            print target
            if target == needle:
                return i
        return -1
if __name__ == '__main__':
    a = Solution()
    haystack = "mississippi"
    needle = "pi"
    print a.strStr(haystack, needle)