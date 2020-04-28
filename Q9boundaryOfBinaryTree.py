# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def boundryOfBinaryTree(self, root):
        """

        :param root:
        :return:
        """
        if root == None:
            return None
        leafres = list()
        leftbound = list()
        rightbound = list()

        leafNode = self.getLeafNode(root, leafres)
        leftBound = self.getLeftBoundaryNodes(root, leftbound)
        rightBound = self.getRightBoundaryNodes(root.right,rightbound)

        res =  leftBound + leafNode + rightBound

        return res

    def getLeafNode(self, root, res):

        if(root):
            print root.val, "val"
            self.getLeafNode(root.left,res)
            if(root.left == None and root.right == None):
                res.append(root.val)
            self.getLeafNode(root.right,res)
        return res

    def getLeftBoundaryNodes(self, root, res):
        if(root):
            if(root.left):
                res.append(root.val)
                self.getLeftBoundaryNodes(root.left,res)
            elif(root.right):
                res.append(root.val)
                self.getLeftBoundaryNodes(root.left, res)
        return res

    def getRightBoundaryNodes(self, root, res):
        if root:
            if(root.right):
                self.getLeftBoundaryNodes(root.right,res)
                res.append(root.val)
            elif(root.left):
                self.getLeftBoundaryNodes(root.right, res)
                res.append(root.val)
        return res


root = TreeNode(20)
root.left = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)

root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right = TreeNode(22)
root.right.right = TreeNode(25)
sol = Solution()
print sol.boundryOfBinaryTree(root)
