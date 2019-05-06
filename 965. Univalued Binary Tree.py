# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.check(root, root.val)

    def check(self, node, value):
        if node == None:
            return True
        else:

            if node.val != value:
                return False

            l = self.check(node.left, value)
            r = self.check(node.right, value)

            return l and r

