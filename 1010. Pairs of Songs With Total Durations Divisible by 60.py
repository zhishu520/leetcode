class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """

        arr = [0] * 60

        l = len(time)
        for i in range(0, l):
            arr[time[i] % 60] += 1

        r = arr[0] * (arr[0] - 1)
        r += arr[30] * (arr[30] - 1)
        for i in range(1, 60):
            if i != 30:
                r += arr[60-i] * arr[i]

        return r / 2


if __name__ == '__main__':
    s = Solution()
    r = s.numPairsDivisibleBy60([60, 60, 60])
    print(r)
