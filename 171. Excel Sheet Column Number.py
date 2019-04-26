class Solution(object):
    def titleToNumber(self, s):
        r = 0
        for i in s:
            r *= 26
            r += ord(i) - ord('A') + 1
        return r




if __name__ == '__main__':
    s = Solution()
    s.titleToNumber("ABC")


