class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        for i in range(len(words) - 1):
            if not self.isLess(words[i], words[i+1], order):
                return False

        return True

    def isLess(self, a, b, order):

        m = min(len(a), len(b))

        print(a, b)
        for i in range(1):
            if order.index(a[i]) > order.index(b[i]):
                return False

        return True




if __name__ == '__main__':
    s = Solution()
    r = s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
    print(r)
