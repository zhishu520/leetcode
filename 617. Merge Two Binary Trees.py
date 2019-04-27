# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        r = None

        if t1 or t2:
            r = TreeNode(0)

        if t1:
            r.val += t1.val

        if t2:
            r.val += t2.val

        if r:
            l1 = t1.left if t1 else None
            l2 = t2.left if t2 else None
            r.left = self.mergeTrees(l1, l2)

            r1 = t1.right if t1 else None
            r2 = t2.right if t2 else None
            r.right = self.mergeTrees(r1, r2)

        return r





