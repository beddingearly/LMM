# coding=utf-8
'''
@Time    : 2018/11/27 10:10
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 11_Container_With_Most_Water.py
@Software: PyCharm
'''


class Solution(object):
    # Violent
    # def maxArea(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     s = 0
    #     for i in range(len(height)):
    #         for j in range(i + 1, len(height)):
    #             if height[i] > height[j]:
    #                 lowH = height[j]
    #             else:
    #                 lowH = height[i]
    #             W = j-i
    #             tmp = lowH * W
    #             if tmp > s:
    #                 s = tmp
    #     return s

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype:
        """
        l = 0
        r = len(height) - 1
        h = (height[r] if (height[l] > height[r]) else height[l])
        s = h * (r - l)
        while l < r:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            h = (height[r] if (height[l] > height[r]) else height[l])
            s = max(s, (r-l)*h)
        return s


if __name__ == '__main__':
    a = Solution()
    print a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
