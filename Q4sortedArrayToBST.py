# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, nums, start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.buildTree(nums, start, mid)
        node.right = self.buildTree(nums, mid + 1, end)
        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        return self.buildTree(nums, 0, len(nums))
