class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.a = []

        self.a.append("QWERTYUIOPqwertyuiop")
        self.a.append("ASDFGHJKLasdfghjkl")
        self.a.append("ZXCVBNMzxcvbnm")

        r = []
        for i in words:
            if self.isOneLine(i):
                r.append(i)

        return r



    def isOneLine(self, s):
        if len(s) == 1:
            return True

        if self.a[0].find(s[0]) != -1:
            l = 0
        elif self.a[1].find(s[0]) != -1:
            l = 1
        else:
            l = 2

        for i in s:
            if self.a[l].find(i) == -1:
                return False

        return True




if __name__ == '__main__':
    s = Solution()
    r = s.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(r)
