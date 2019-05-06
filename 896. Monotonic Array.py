class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        isUp = None
        pre = A[0]

        for i in A:

            if isUp == None:

                if i - pre > 0:
                    isUp = True
                    pre = i
                    continue

                if i - pre < 0:
                    isUp = False
                    pre = i
                    continue

            if isUp == True and i - pre < 0:
                return False

            if isUp == False and i - pre > 0:
                return False

            pre = i



        return True
