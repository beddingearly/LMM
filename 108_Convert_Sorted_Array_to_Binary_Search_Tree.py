#coding=utf-8
'''
@Time    : 2018/12/14 09:36
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 108_Convert_Sorted_Array_to_Binary_Search_Tree.py
@Software: PyCharm
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = nums[len(nums)/2]