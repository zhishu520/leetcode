
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ret = []
        ret.append([1])

        for i in range(1, numRows):
            temp = []

            for j in range(0, i):
                if j - 1 >= 0:
                    temp.append(ret[i-1][j-1] + ret[i-1][j])
                else:
                    temp.append(1)

            temp.append(1)

            ret.append(temp)
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.generate(4))
