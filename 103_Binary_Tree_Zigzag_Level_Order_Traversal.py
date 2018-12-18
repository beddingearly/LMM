#coding=utf-8
'''
@Time    : 2018/12/4 23:46
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 103_Binary_Tree_Zigzag_Level_Order_Traversal.py
@Software: PyCharm

给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

      3
   /    \
  9     20
 / \   /  \
5   6 15   7

返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
   l r    l  r  9
3 20 9    15 7  9 5 6 15
这个题，层很重要，不同的层
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return [[]]
        elif root.right == None and root.left == None:
            return [[root.val]]
        d = deque([])
        result = [[root.val]]
        d.appendleft(root.left)
        d.appendleft(root.right)
        flag = 0
        level = 2
        tmp = []
        while len(d) != 0:
            node = d.pop()
            level -= 1
            if node != None:
                tmp.append(node.val)
                if node.left != None:
                    d.appendleft(node.left)
                if node.right != None:
                    d.appendleft(node.right)
            if level == 0:
                if flag == 1:
                    result.append(tmp)
                    flag = 0
                else:
                    tmp.reverse()
                    result.append(tmp)
                    flag = 1
                tmp = []
                level = len(d)
        return result

if __name__ == '__main__':
    a = Solution()
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    print a.zigzagLevelOrder(t)