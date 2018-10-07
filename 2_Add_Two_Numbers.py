# coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = ListNode(0)
        p = a
        flag = 0
        while l1 and l2:
            tmp = l1.val + l2.val + flag
            if tmp > 9:
                tmp -= 10
                flag = 1
            else:
                flag = 0
            p.next = ListNode(tmp)
            p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            if flag == 1:  # 有进位
                l1.val += flag
                if l1.val > 9:
                    l1.val -= 10
                    flag = 1
                else:
                    flag = 0
                p.next = ListNode(l1.val)
                l1 = l1.next
                p = p.next
            else:
                p.next = l1
                break
        while l2:
            if flag == 1:
                l2.val += flag  # 有进位
                if l2.val > 9:
                    l2.val -= 10
                    flag = 1
                else:
                    flag = 0
                p.next = ListNode(l2.val)
                l2 = l2.next
                p = p.next
            else:
                p.next = l2
                break

        if flag == 1:
            p.next = ListNode(1)
            # p = p.next
        return a.next

    def new_print(self, x):
        while x:
            print x.val
            x = x.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(8)
    b = ListNode(0)
    c = Solution()
    d = c.addTwoNumbers(a, b)
    c.new_print(d)
