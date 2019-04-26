class Solution(object):

    def xor(self, a, b):
        if a == b:
            return ("0" if a == "0" else "1", "0")

        else:
            return ("0", "1")

    def addBinary(self, a, b):
        la = len(a)
        lb = len(b)
        if la > lb:
            a, b = b, a
            la, lb = lb, la

        s = ""
        t = "0"
        for i in range(0, lb):
            if i < la:
                na = a[la - i - 1]
            else:
                na = "0"
            nb = b[lb - i - 1]

            t1, ni = self.xor(na, nb)
            t2, nt = self.xor(ni, t)
            _, t = self.xor(t1, t2)

            s += nt

        if t == "1":
            s += t

        return s[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))


