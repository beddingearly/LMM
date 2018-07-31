#coding=utf-8
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        m -= 1
        n -= 1
        stack = []
        while(head):
            val = head.val
            head = head.next
            stack.append(val)
        for i in range(m, (n+m)/2+1):
            tmp = stack[i]
            stack[i] = stack[m+n-i]  # remember
            stack[m+n-i] = tmp

        return stack


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    b = Solution()
    print b.reverseBetween(a, 2, 3)
