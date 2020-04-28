# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        return self.treetraversal(root, res)
    def treetraversal(self, root, res):
        if(root):
            self.treetraversal(root.left, res)
            self.treetraversal(root.right, res)
            res.append(root.val)
        return res