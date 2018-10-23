#coding=utf-8
'''
@Time    : 2018/10/19 09:34
@Author  : Zt.Wang
@Email   : wztong@cug.edu.cn
@File    : KMP.py
@Software: PyCharm
'''
class KMP(object):
    def __init__(self, s, pattern):
        self.next = [-1] * len(pattern)
        self.str = s
        self.pattern = pattern
    def cal_next(self):
        self.next[0] = -1

        for i in range(1, len(self.pattern), 1):
            j = self.next[i-1]  # 匹配位数
            while self.pattern[j+1] != self.pattern[i] and j >= 0:
                j = self.next[j]
            if self.pattern[i] == self.pattern[j+1]:
                self.next[i] = j + 1
            else:
                self.next[i] = -1

    def kmp(self):
        self.cal_next()
        k = -1
        for i in range(len(self.str)):

            while k > -1 and self.pattern[k + 1] != self.str[i]:
                k = self.next[k]

            if self.pattern[k + 1] == self.str[i]:
                k += 1

            if k == len(self.pattern) - 1:
                return i - len(self.pattern) + 1
        return -1

    def kmpRyf(self):
        i = 0
        while i < len(self.str):
            #print self.str[i:]
            for j in range(len(self.pattern)):
                if self.pattern[j] == self.str[i]:
                    #print j
                    if j == 1:
                        print self.str[i:]
                    if j == len(self.pattern)-1:  # 最后一个都匹配相同
                        return i-len(self.pattern)+1
                    i += 1
                else:  # 匹配不同
                    i = i + self.next[j] + 1
                    break
        return -1


if __name__ == '__main__':
    k = KMP('ababaaababaa', 'aab')
    print k.str
    print k.pattern
    k.cal_next()
    #print k.kmp()
    print k.kmpRyf()
    #print k.next