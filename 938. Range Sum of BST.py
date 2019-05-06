# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        sum = 0
        self.sum(root, L, R, sum)
        return sum

    def sum(self, node, l, r, sum):
        if node == None:
            return 0
        else:

            if node.val > l and node.val < r:
                sum += l

            self.sum(node.left)
            self.sum(node.right)






