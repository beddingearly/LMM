#coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None


if __name__ == '__main__':
    a = ListNode(4)

    a2 = ListNode(5)
    a.next = a2
    a3 = ListNode(1)
    a2.next = a3
    a4 = ListNode(3)
    a3.next = a4
    c = Solution()
    c.deleteNode(a2)
    while(a):
        print a.val
        a = a.next

