# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    stack = list()

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.inorder(root)
            temp = TreeNode(self.stack.pop())
            while (self.stack):
                newNode = TreeNode(self.stack.pop())
                newNode.right = temp
                temp = newNode
            return temp

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.stack.append(root.val)
            self.inorder(root.right)