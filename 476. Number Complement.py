class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """


        ret = 0
        cnt = 0
        while num > 0:
            ret += (1 if num % 2 == 0 else 0) * (1 << cnt)
            num = num >> 1
            cnt += 1

        return ret


if __name__ == '__main__':
    s = Solution()
    print s.findComplement(2)
