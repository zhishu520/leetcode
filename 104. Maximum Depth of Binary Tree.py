
class Solution(object):
    def maxDepth(self, root):
        cnt = 0
        r = self.search(root, cnt)
        return r

    def search(self, root, cnt):
        if root == None:
            return cnt
        else:
            return max(self.search(root.left, cnt+1), self.search(root.right, cnt+1))