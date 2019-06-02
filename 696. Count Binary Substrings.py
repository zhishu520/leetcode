class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)
        if l == 0:
            return 0

        cnt = 1
        c = s[0]
        rt = []

        for i in range(1, l):
            if s[i] == c:
                cnt += 1
            else:
                rt.append(cnt)
                c = s[i]
                cnt = 1
        rt.append(cnt)

        st = 0
        for i in range(0, len(rt)-1):
            st += min(rt[i], rt[i+1])
        return st


