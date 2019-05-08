class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num < 0:
            return "-" + self.convertToBase7(-num)

        s = ""
        while True:
            s += str(num % 7)
            num /= 7
            if num == 0:
                break

        return s[::-1]


