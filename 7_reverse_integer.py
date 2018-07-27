# coding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x < -2**31 or x > 2**31-1:
            return 0
        while(True):
            if x % 10 == 0:
                x /= 10
            else:
                break
        if x < 0:
            tmp = str(x)[1:]
            result = int('-' + tmp[::-1])
        else:
            result = int(str(x)[::-1])
        if result < -2**31 or result > 2**31-1:
            return 0
        else:
            return result
    def reverse2(self, x):
        if x == 0 or x < -2**31 or x > 2**31-1:
            return 0
        while(True):
            if x % 10 == 0:
                x /= 10
            else:
                break
        a = list(str(x))
        a.reverse() # list
        # a.pop # stack
        # result = reduce(lambda x,y:y+x,a) # reduce
        result = "".join(a)
        if result[-1] == '-':
            result = result[-1] + result[0:-1]

        result = int(result)
        if result < -2**31 or result > 2**31-1:
            return 0
        return result


if __name__ == '__main__':
    a = Solution()
    print a.reverse2(-1534230)