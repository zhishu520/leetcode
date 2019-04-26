class Solution(object):
    def levelOrderBottom(self, root):
        r = []
        cnt = 0
        self.search(root, cnt, r)

        s = len(r)
        for i in range(0, s/2):
            r[i], r[s-i-1] = r[s-i-1], r[i]

        return r

    def search(self, root, cnt, r):
        if root:
            if len(r) <= cnt:
                r.append([root.val])
            else:
                r[cnt].append(root.val)

            self.search(root.left, cnt + 1, r)
            self.search(root.right, cnt + 1, r)
