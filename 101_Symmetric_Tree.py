# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        elif root.left == None or root.right == None:
            return False
        else:
            return root.right.val == root.left.val and self.check(root.left, root.right)

    def check(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            return node1.val == node2.val and self.check(node1.left, node2.right) and self.check(node1.right,
                                                                                                 node2.left)

    def isSymmetric(self, root):
        '''
        :param root:
        :return:
        '''
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        elif root.left == None or root.right == None:
            return False
        else:
            d = deque([])
            l = root.left
            r = root.right
            d.appendleft(l)
            d.append(r)
            while len(d) != 0:
                leftnode = d.popleft()
                rightnode = d.pop()
                if leftnode == None and rightnode == None:
                    return True
                elif leftnode == None or rightnode == None:
                    return False
                else:
                    if leftnode.val == rightnode.val:
                        d.appendleft(l.left)
                        d.append(r.right)
                        d.appendleft(l.right)
                        d.append(r.left)
                    else:
                        return False
            return True


if __name__ == '__main__':
    a = Solution()
    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode()
