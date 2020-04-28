# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        return (self.traverse(root, res))

    def traverse(self, root, res):
        if root:
            self.traverse(root.left, res)
            res.append(root.val)
            self.traverse(root.right, res)
        print res
        return res

