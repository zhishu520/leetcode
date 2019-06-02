class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        s1 = []

        for i in S:
            if i == '#':
                if len(s1) > 0:
                    s1.pop()
            else:
                s1.append(i)

        s2 = []

        for i in T:
            if i == '#':
                if len(s2) > 0:
                    s2.pop()
            else:
                s2.append(i)

        return s1 == s2


