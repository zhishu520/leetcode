# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return None;

        t = TreeNode(root.val)

        if root.right:
            l = self.invertTree(root.right)
            t.left = l

        if root.left:
            r = self.invertTree(root.left)
            t.right = r

        return t
