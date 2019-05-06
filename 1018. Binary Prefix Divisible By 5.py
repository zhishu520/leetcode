class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """

        r = []
        n = 0
        for i in A:
            n = n * 2 + i
            r.append(n % 5 == 0)

        print(r)

        return r

if __name__ == '__main__':
    s = Solution();
    s.prefixesDivBy5([0,1,1,1])