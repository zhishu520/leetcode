# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """


        if len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1
        mid =  (right + left) / 2

        t = TreeNode(nums[mid])
        t.left = self.sortedArrayToBST(nums[:mid])
        t.right = self.sortedArrayToBST(nums[mid+1])
        return t

