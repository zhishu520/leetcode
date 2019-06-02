"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        self.rt = []
        self.search(root, 0)
        return self.rt

    def search(self, root, level):

        if not root:
            return

        if level >= len(self.rt):
            self.rt.append([root.val])
        else:
            self.rt[level].append(root.val)

        for i in root.children:
            self.search(i, level + 1)


