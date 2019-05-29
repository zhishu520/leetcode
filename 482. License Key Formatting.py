class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        if S == "":
            return ""


        S = S.replace("-", "")

        l = len(S)
        start = l % K


        r = ""
        for i in range(l):
            if (i - start) % K == 0 and i != 0:
                r += "-" + S[i]
            else:
                r += S[i]

        return r.upper()


