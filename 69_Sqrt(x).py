class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x/2+1
        while low <= high:
            mid = (low + high) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid+1
            else:
                high = mid-1
        return (high+low)/2
if __name__ == '__main__':
    a = Solution()
    x = 9
    print a.mySqrt(x)