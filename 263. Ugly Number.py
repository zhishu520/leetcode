class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 1:
            return False


        while num != 1:
            do = False
            if num % 2 == 0:
                num /= 2
                do = True

            if num % 3 == 0:
                num /= 3
                do = True

            if num % 5 == 0:
                num /= 5
                do = True

            if not do:
                return False

        return True
