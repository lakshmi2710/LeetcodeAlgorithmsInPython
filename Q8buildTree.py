# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if (len(preorder) <= 0 or len(inorder) <= 0):
            return
        root = TreeNode(preorder[0])
        if (root):
            indexInorder = inorder.index(root.val)
            root.left = self.buildTree(preorder[1:indexInorder + 1], inorder[:indexInorder])
            root.right = self.buildTree(preorder[indexInorder + 1:], inorder[indexInorder + 1:])
        return root
