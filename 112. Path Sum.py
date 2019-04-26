class Solution(object):
    def hasPathSum(self, root, sum):
        return self.search(root, 0, sum)

    def search(self, root, sum, target):
        if root == None:
            return False

        if root.left == None and root.right == None:
            return sum + root.val == target
        else:
            l = self.search(root.left, sum + root.val, target)
            r = self.search(root.right, sum + root.val, target)
            return l or r

