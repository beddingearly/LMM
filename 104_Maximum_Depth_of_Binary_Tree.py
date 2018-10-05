# coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            left = 1 + self.maxDepth(root.left)
            print('left', left)
            right = 1 + self.maxDepth(root.right)
            print('right', right)
            return max(right, left)


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
    b.maxDepth(a)
