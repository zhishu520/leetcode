# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        if root == None:
            return True

        if root.left and root.left.val > root.val:
            return False

        if root.right and root.right.val < root.val:
            return False

        l = self.isValidBST(root.left)
        r = self.isValidBST(root.right)

        return l and r

