class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        p5 = 0
        p10 = 0

        for i in bills:
            if i == 5:
                p5 += 1
            elif i == 10:
                if p5 == 0:
                    return False
                else:
                    p5 -= 1
                    p10 += 1
            else:
                if p5 >= 3 and p10 == 0:
                    p5 -= 3
                elif p5 > 0 and p10 > 0:
                    p5 -= 1
                    p10 -= 1
                else:
                    return False

        return True
