#coding=utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        while(head):
            val = head.val
            head = head.next
            result.append(str(val))
        result1 = ''.join(result)
        result.reverse()
        result2 = ''.join(result)
        if result1 == result2:
            return True
        else:
            return False


if __name__ == '__main__':
    a = ListNode(2)
    a.next = ListNode(3)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(2)
    b = Solution()
    print b.isPalindrome(a)



