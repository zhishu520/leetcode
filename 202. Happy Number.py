

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        d = {}

        while n != 1:
            t = n
            n = 0
            while t:
                n += (t % 10) * (t % 10)
                t = int(t/10)

            if d.has_key(n):
                return False
            else:
                d.setdefault(n, True)

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))









