# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists_backup(self, l1, l2):
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

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        p1 = l1
        p2 = l2
        head = ListNode(-1)
        p = head
        while p1 and p2:
            if p1.val <= p2.val:
                pp = ListNode(p1.val)
                p.next = pp
                p1 = p1.next
            elif p1.val > p2.val:
                pp = ListNode(p2.val)
                p.next = pp
                p2 = p2.next
            p = p.next
        if p1 is None:
            p.next = p2
        elif p2 is None:
            p.next = p1
        head = head.next
        while(head):
            print head.val
            head = head.next
        return head


if __name__ == '__main__':
    a = Solution()
    b1 = ListNode(2)
    #b1.next = ListNode(2)
    #b1.next.next = ListNode(3)

    b2 = ListNode(1)
    #b2.next = ListNode(3)
    #b2.next.next = ListNode(4)
    a.mergeTwoLists(b1, b2)