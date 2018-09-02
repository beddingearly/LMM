#  coding=utf-8
# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        d = deque([])
        d.append(root)
        result = []
        result.append([root.val])
        res = []
        current_level_num = 1
        next_level_num = 0
        while len(d) != 0:
            node = d.popleft()
            current_level_num -= 1
            if node.left != None:
                res.append(node.left.val)
                d.append(node.left)
                next_level_num += 1
            if node.right != None:
                res.append(node.right.val)
                d.append(node.right)
                next_level_num += 1
            if current_level_num == 0:
                current_level_num = next_level_num
                next_level_num = 0
                if len(res) != 0:
                    result.append(res)
                res = []
        print result[::-1]
        return result[::-1]

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
    b.levelOrderBottom(a)
