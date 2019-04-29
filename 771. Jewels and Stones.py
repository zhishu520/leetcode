class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        r = 0
        for i in J:
            r += S.count(i)
        return r

