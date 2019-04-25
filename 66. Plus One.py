class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = len(digits)

        r = []

        t = 1
        for i in range(0, s):
            n = t + digits[s-i-1]
            r.append(n % 10)
            t = int(n / 10)

        if not t is 0:
            r.append(t)

        s = len(r)
        for i in range(0, len(r)/2):
            tt = r[s-i-1]
            r[s-i-1] = r[i]
            r[i] = tt

        return r

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9]))
