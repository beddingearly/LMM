# coding=utf-8
# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
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

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid_index_inorder = inorder.index(preorder[0])
        new_inorder_left = inorder[:mid_index_inorder]
        new_inorder_right = inorder[mid_index_inorder + 1:]
        print new_inorder_right

        new_preorder_left = preorder[1:mid_index_inorder + 1]
        new_preorder_right = preorder[mid_index_inorder + 1:]

        root.left = self.buildTree(new_preorder_left, new_inorder_left)
        root.right = self.buildTree(new_preorder_right, new_inorder_right)

        return root


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

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    b = Solution()
    b.buildTree(preorder, inorder)
