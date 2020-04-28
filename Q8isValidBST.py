# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = list()
        self.inorder(root, output)

        for i in range(len(output) - 1):
            if output[i] >= output[i + 1]:
                return False
        return True

    def inorder(self, root, output):
        if root == None:
            return
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)

