# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.realroot = root
        return self.search(root, k)

    def search(self, root, k):

        if root == None:
            return False

        if self.find(root.left, k - root.val) or self.find(root.right, k - root.val):
            return True
        else:
            l = self.findTarget(root.left, k)
            r = self.findTarget(root.right, k)
            return l or r

    def find(self, root, target):
        if root == None:
            return False

        if root.val == target:
            return True

        return self.find(root.left if target < root.val else root.right, target)

