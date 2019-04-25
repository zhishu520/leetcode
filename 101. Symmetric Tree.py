
class Solution(object):
    def isSymmetric(self, root):
        dist = None
        t = self.create(root, dist)
        return self.isSameTree(root, t)

    def pnt(self, r):
        if r:
            print(r.val)
            self.pnt(r.left)
            self.pnt(r.right)

    def create(self, source, dist):
        if source == None:
            dist = None;
        else:
            dist = TreeNode(source.val)
            dist.right = self.create(source.left, dist.right)
            dist.left = self.create(source.right, dist.left)
            return dist

    def isSameTree(self, p, q):
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.val != q.val:
            return False

        sl = self.isSameTree(p.left, q.left)
        sr = self.isSameTree(p.right, q.right)

        return sl and sr
