# coding=utf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str = ''
        length = len(strs)
        if length == 0:
            return ''
        num = [len(i) for i in strs]
        for i in range(min(num)):
            flag = strs[0][i] ###
            for j in strs:
                if j[i] != flag:
                    return str
            str += flag

        return str


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    #strs = ["dog", "racecar", "car"]
    strs = []
    a = Solution()
    print a.longestCommonPrefix(strs)