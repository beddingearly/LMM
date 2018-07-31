#coding=utf-8
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        point = head
        l = []
        while(point):
            val = point.val
            point = point.next
            l.append(val)
        result = [i for i in set(l)]
        '''result = l
        for i in l:
            if l.count(i) > 1:
                result.remove(i)'''
        result.sort()
        return result

if __name__ == '__main__':
    a = ListNode(7)
    a.next = ListNode(6)
    a.next.next = ListNode(4)
    a.next.next.next = ListNode(1)
    b = Solution()
    print b.deleteDuplicates(a)