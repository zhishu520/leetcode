# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        self.min = 10000
        self.search(root, 1)
        return self.min

    def search(self, root, level):

        if root == None:
            return

        if root.left == None and root.right == None:
            if self.min > level:
                self.min = level

        self.search(root.left, level + 1)
        self.search(root.right, level + 1)



