class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        ls = len(s)
        lt = len(t)

        if ls != lt:
            return False

        dica = {}
        dicb = {}

        for i in range(0, ls):
            c = s[i]
            b = t[i]
            d = ord(s[i]) - ord(t[i])

            if dica.has_key(c):
                if dica[c] != d:
                    return False
            else:
                dica.setdefault(c, d)

            if dicb.has_key(b):
                if dicb[b] != d:
                    return False
            else:
                dicb.setdefault(b, d)

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("ab", "aa"))


