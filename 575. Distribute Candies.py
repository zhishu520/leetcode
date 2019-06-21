class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        l = len(candies)
        s = set(candies)
        ls = len(s)
        return ls if ls < l / 2 else l / 2

if __name__ == '__main__':
    s = Solution()
    s.distributeCandies([1,2,3,2])
