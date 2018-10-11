class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        a = s.split(' ')
        for i in range(len(a)):
            a[i] = a[i][::-1]
        for j in a:
            result += j + ' '
        return result[:-1]