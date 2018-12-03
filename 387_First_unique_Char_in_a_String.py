class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # l = list(s)
        # ll = []
        # for i in range(len(l)):
        #     num = l.count(l[i])
        #     if num == 1:
        #         return i
        # return -1
        for i in s:
            if i in s[s.index(i)+1:]:
                print s.index(i)
                continue
            else:
                return s.index(i)

        return -1
if __name__ == '__main__':
    s = "cca"
    #s = 'loveleetcode'
    a = Solution()
    print a.firstUniqChar(s)
