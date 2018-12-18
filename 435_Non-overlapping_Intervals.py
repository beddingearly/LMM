#coding=utf-8
'''
@Time    : 2018/12/17 15:16
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 435_Non-overlapping_Intervals.py
@Software: PyCharm
'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        poplist = []
        print intervals
        intervals = sorted(intervals, key=lambda x: x[1])  #
        length = len(intervals)-1
        i = 0
        cot = 0
        while i != length:
            if intervals[i].end == intervals[j].end:
                j = j if (intervals[i].end - intervals[i].start) > (intervals[j].end - intervals[j].start) else i
                cot += 1
            if intervals[i][1] > intervals[i+1][0]:
                tmp = intervals[i] if (intervals[i][1] - intervals[i][0]) > (intervals[i+1][1] - intervals[i+1][0]) else intervals[i+1]
                intervals.remove(tmp)
                i -= 1
                length -= 1
                poplist.append(tmp)
            i += 1
        print intervals
        print poplist

if __name__ == '__main__':
    s = Solution()
    s.eraseOverlapIntervals([[1,2],[1,2],[1,2]])

