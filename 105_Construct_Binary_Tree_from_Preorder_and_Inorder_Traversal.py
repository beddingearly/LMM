# coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

    def preorder(self, root):
        if root == None:
            return
        print root.val
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root == None:
            return
        self.preorder(root.left)
        print root.val
        self.preorder(root.right)

    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)


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
    b.preorder(a)
