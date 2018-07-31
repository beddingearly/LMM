# coding=utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        cot = 0
        flag = 0
        tmp = 0
        for i in range(len(s)-1):
            print cot
            if flag == 0:
                if alpha[s[i]] >= alpha[s[i + 1]]:
                    cot += alpha[s[i]]
                else:
                    tmp = alpha[s[i + 1]]-alpha[s[i]]
                    flag = 1
                    if i == len(s)-2:
                        cot += tmp
            else:
                flag = 0
                cot += tmp
        if flag == 0:
            cot += alpha[s[-1]]
        return cot

if __name__ == '__main__':
    s = "LVIII"
    a = Solution()
    print a.romanToInt(s)
