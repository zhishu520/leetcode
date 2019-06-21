# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.rt = None
        self.pre = None
        self.search(root)
        return self.rt

    def search(self, root):

        if root.left:
            self.search(root.left)

        t = TreeNode(root.val)
        if self.rt == None:
            self.rt = t
            self.pre = t
        else:
            self.pre.right = t
            self.pre = t

        if root.right:
            self.search(root.right)



