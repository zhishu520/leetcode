"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        self.rt = []
        self.search(root)
        return self.rt



    def search(self, root):
        if root == None:
            return

        self.rt.append(root.val)

        for i in root.children:
            self.search(i)



