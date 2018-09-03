# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        a = headA
        b = headB
        la = 0
        lb = 0
        while a.next:
            la += 1
            a = a.next
        while b.next:
            lb += 1
            b = b.next
        if a != b:
            return None
        a = headA
        b = headB
        if la > lb:
            for i in range(la - lb):
                a = a.next
        else:
            for i in range(lb - la):
                b = b.next
        while a != b:
            a = a.next
            b = b.next
        return a
