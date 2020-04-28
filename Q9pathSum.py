# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = []
    pathsum = 0

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return
        sum = sum - root.val
        print sum, root.val
        if (root.left == None and root.right == None and sum == 0):
            return True
        else:
            if (self.hasPathSum(root.left, sum)) or (self.hasPathSum(root.right, sum)):
                return True
