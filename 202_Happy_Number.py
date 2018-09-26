#coding=utf-8
class Solution(object):
    def x_x(self, i):
        return i * i
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = []
        if n == 1:
            return True
        flag = 0
        while True:
            c = len(str(n))
            while c == 1:
                n = self.x_x(n)
                c = len(str(n))
                print n
            t = n % 10
            sum = self.x_x(t)
            if flag == 0:
                c = len(str(n))
                t = n % 10
                sum = self.x_x(t)
                flag = 1
            for i in range(c-1, 0, -1):
                tmp = n/(10**i)
                n -= tmp*(10**i)
                sum += self.x_x(tmp)
            n = sum
            print n
            if sum == 1:
                return True
            fast = sum
            if fast in slow:
                return False
            slow.append(sum)

if __name__ == '__main__':
    a = Solution()
    print a.isHappy(7)