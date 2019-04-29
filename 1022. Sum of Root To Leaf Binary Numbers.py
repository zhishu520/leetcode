class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.s(root, 0)

    def s(self, root, n):
        if root.left == None and root.right == None:
            return n*2 + root.val
        else:
            l, r = 0, 0
            if root.left:
                l = self.s(root.left, n * 2 + root.val)
            if root.right:
                r = self.s(root.right, n * 2 + root.val)
            return l + r

