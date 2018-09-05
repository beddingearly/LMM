# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        d = []
        qu = deque([])
        if root == None:
            return False
        qu.append(root)
        while len(qu) != 0:
            node = qu.pop()
            if node.val in d:
                return True
            if node.left != None:
                qu.append(node.left)
            if node.right != None:
                qu.append(node.right)
            d.append(k - node.val)
            print d
        return False


if __name__ == '__main__':
    '''
         1
       2   3
    4   5  6  7
    '''
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(5)
    a.right.left = TreeNode(6)
    a.right.right = TreeNode(7)

    b = Solution()
    print b.findTarget(a, 5)
