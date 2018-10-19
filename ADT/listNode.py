#coding=utf-8
class linkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    l = linkNode(-1)
    p = l
    for i in range(3):
        p.next = linkNode(i)
        p = p.next
    p.next = l
    a = l
    while a:
        print a.val
        a = a.next

