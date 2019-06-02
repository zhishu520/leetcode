class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        self.res = []
        self.deal("", S)
        return self.res


    def deal(self, pre, after):
        if after == "":
            self.res.append(pre)
            return

        nafter =  after[1:]

        if after[0].isdigit():
            self.deal(pre[:] + after[0], nafter)
            return

        self.deal(pre[:] + after[0].upper(), nafter)
        self.deal(pre[:] + after[0].lower(), nafter)


if __name__ == '__main__':
    s = Solution()
    print s.letterCasePermutation("a1b2")
        

