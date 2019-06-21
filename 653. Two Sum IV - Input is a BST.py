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

        if root == None:
            return False

        if hasattr(self, "realroot") == False:
            self.realroot = root

        def find(root, target, ban):
            if root == None:
                return False

            if root.val == target and root != ban:
                return True

            return find(root.left if target < root.val else root.right, target, ban)


        if find(self.realroot, k - root.val, root):
            return True

        if find(self.realroot, k - root.val, root):
            return True

        return self.findTarget(root.left, k) or self.findTarget(root.right, k)


