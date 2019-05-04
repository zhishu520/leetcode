class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        cnt = [1000] * 26

        for i in A:
            t = [0] * 26
            for j in i:
                t[ord(j) - ord("a")] += 1

            for j in range(0, 26):
                if t[j] < cnt[j]:
                    cnt[j] = t[j]

        r = []
        for i in range(0, len(cnt)):
            for j in range(0, cnt[i]):
                r.append(chr(ord("a") + i))

        return r

