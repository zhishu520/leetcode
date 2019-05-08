class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """


        S = [0] * 26
        T = [0] * 26

        for i in s:
            S[ord(i) - ord('a')] += 1
        for i in t:
            T[ord(i) - ord('a')] += 1

        for i in range(26):
            if S[i] != T[i]:
                return chr(i + ord('a'))



