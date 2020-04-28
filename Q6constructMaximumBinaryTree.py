# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        index = self.getMaxIndex(nums)
        if (index == None):
            return

        node = TreeNode(nums[index])
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return node

    def getMaxIndex(self, nums):
        if len(nums) < 1:
            return
        max = nums[0]
        for i in range(len(nums)):
            if nums[i] >= max:
                max = nums[i]
                index = i
            else:
                continue
        return index