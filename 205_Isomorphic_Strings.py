class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ss = [0] * len(s)
        tt = [0] * len(t)
        sss = {}
        ttt = {}
        for i in range(len(s)):
            if sss.has_key(s[i]):
                ss[i] = sss[s[i]]
            else:
                sss[s[i]] = i
                ss[i] = i

        for i in range(len(t)):
            if ttt.has_key(t[i]):
                tt[i] = ttt[t[i]]
            else:
                ttt[t[i]] = i
                tt[i] = i
        print ss
        print tt
        print sss
        print ttt
        if ss == tt:
            return True
        else:
            return False
if __name__ == '__main__':
    s = "paper"
    t = "title"
    a = Solution()
    print a.isIsomorphic(s, t)
