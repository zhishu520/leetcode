class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            arr = [1, 2]

            for i in range(2, n):
                arr.append(arr[i-1] + arr[i-2])
            return arr[n-1]
