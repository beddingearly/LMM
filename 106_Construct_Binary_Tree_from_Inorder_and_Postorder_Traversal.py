#coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 找到中序和后序的对应关系，中序为【左，根，右】，后序为【左，右，根】
        if postorder == []:
            return 0
        node = TreeNode(postorder[-1])

        left_inorder_tailer = inorder.index(postorder[-1])

        left_inorder = inorder[:left_inorder_tailer]
        right_inorder = inorder[left_inorder_tailer+1:]

        left_postorder = postorder[:left_inorder_tailer]
        right_postorder = postorder[left_inorder_tailer:-1]  #右子树第一个

        node.left = self.buildTree(left_inorder, left_postorder)
        node.right = self.buildTree(right_inorder, right_postorder)

        return node