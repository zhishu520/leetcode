# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return True

        def depth(root, level):
            if root == None:
                return level
            l = depth(root.left, level + 1)
            r = depth(root.right, level + 1)
            return max(l, r)

        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(depth(root.left, 0) - depth(root.right, 0)) <= 1



