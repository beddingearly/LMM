# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        f = head
        length = 0
        while (f):
            length += 1
            f = f.next
        mid = length / 2
        s = head
        cot = -1
        while cot != mid:
            cot += 1
            res = s
            s = s.next
        return res

