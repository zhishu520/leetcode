# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        a1, a2 = [], []
        self.genarr(root1, a1)
        self.genarr(root2, a2)

        l1 = len(a1)
        l2 = len(a2)

        if l1 != l2:
            return False

        for i in range(0, l1):
            if a1[i] != a2[i]:
                return False
        return True

    def genarr(self, node, arr):
        if node == None:
            return

        if tree.left == None and tree.right == None:
            arr.append(node)
        else:
            self.genarr(node.left, arr)
            self.genarr(node.right, arr)








