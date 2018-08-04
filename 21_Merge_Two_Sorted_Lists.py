# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        l = []
        while(l1):
            l.append(l1.val)
            l1 = l1.next
        while(l2):
            l.append(l2.val)
            l2 = l2.next
        l.sort()
        aa = ListNode(l[0])
        point = aa
        for i in l[1:]:
            node = ListNode(i)
            point.next = node
            point = point.next
        return aa
if __name__ == '__main__':
    a = Solution()
    b1 = ListNode(1)
    b1.next = ListNode(2)
    b1.next.next = ListNode(3)

    b2 = ListNode(1)
    b2.next = ListNode(3)
    b2.next.next = ListNode(4)
    print a.mergeTwoLists(b1, b2)