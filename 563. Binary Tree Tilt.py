# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count=[0]
        def helper(root):
            l,r=0,0
            if root.left:
                l=helper(root.left)
            if root.right:
                r=helper(root.right)
            count[0]+=abs(l-r)
            return l+r+root.val
        helper(root)
        return count[0]