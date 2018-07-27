# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        while(head):
            val = head.val
            stack.append(val)
            head = head.next
        if stack:
            new_head = ListNode(stack.pop())
            point = new_head
            while (stack):
                point.next = ListNode(stack.pop())
                point = point.next
            return new_head
        else:
            return head

if __name__ == '__main__':
    a = ListNode(None)
    #a.next = ListNode(2)
    #a.next.next = ListNode(3)
    #a.next.next.next = ListNode(4)
    b = Solution()
    print b.reverseList(a)

