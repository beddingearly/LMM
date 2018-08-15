#  coding=utf-8
import string


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.translate(None, string.punctuation)  # 去标点符号
        s = ''.join(s.split())  # 去句中空格
        s = s.lower()  # 转化小写
        ss = s[::-1]
        if s == ss:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    s = "A man, a plan, a canal: Panama"
    print a.isPalindrome(s)
