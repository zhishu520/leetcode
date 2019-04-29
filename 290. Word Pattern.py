class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        d = {}
        d2 = {}

        ls = str.split(" ")
        lp = list(pattern)

        lls = len(ls)
        llp = len(lp)
        if lls != llp:
            return False

        for i in range(0, lls):

            c = lp[i]
            s = ls[i]

            if d.has_key(c):
                if d[c] != s:
                    return False
            else:
                d.setdefault(c, s)

            if d2.has_key(s):
                if d2[s] != c:
                    return False
            else:
                d2.setdefault(s, c)

        return True


