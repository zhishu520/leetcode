"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        return self.search(root, 0)


    def search(self, node, x):
        if node == None:
            return x
        else:

            max = 0
            for i in node.children:
                d = self.search(i, x + 1)
                if d > max:
                    max = d
            return 1 + max


