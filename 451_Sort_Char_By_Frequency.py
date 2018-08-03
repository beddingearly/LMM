class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        l = [0]*26
        alpha = []
        ss = ''
        for i in s:
            if i in alpha:
                l[ord(i)-97] += 1
            else:
                l[ord(i)-97] = 1
                alpha.append(i)

        #ll = sorted(d, key=lambda x: d[x], reverse=True)
        # for i in ll:
        #     for j in range(d[i]):
        #         ss += i
        #l.sort()
        return l


if __name__ == '__main__':
    a = Solution()
    s = "cccaaa"
    s = "loveleetcode"
    print a.frequencySort(s)