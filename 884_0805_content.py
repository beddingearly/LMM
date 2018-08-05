#coding=utf-8
class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = 0
        for i in range(len(S)):
            print s
            if s == K:
                #print(K)
                return s[-1]
            elif (ord(S[i]) >= 58 or ord(S[i]) <= 47) and s < 2**63:
                s += 1
                #print s
                #print(len(s))
            elif (ord(S[i]) <= 57 and ord(S[i]) >= 50) and s < 2**63:
                ss = s
                if len(ss * (int(S[i])-1)) < 2**63:
                    s += ss * (int(S[i])-1)
                else:
                    break
            elif (ord(S[i]) >= 48 and ord(S[i]) < 50) and s < 2**63:
                continue
            else:
                break
        #print s
        return s[K]
if __name__ == '__main__':
    a = Solution()
    S = "y959q969u3hb22odq595"
    K = 222280369
    print a.decodeAtIndex(S, K)