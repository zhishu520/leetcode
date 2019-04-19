


class Solution(object):
    def divide(self, dividend, divisor):

        cnt = 0
        if dividend < 0:
            dividend = - dividend
            cnt += 1

        if divisor < 0:
            divisor = - divisor
            cnt += 1

        if cnt == 1:
            result = - (long)(dividend / divisor)
        else:
            result = (long)(dividend / divisor)

        if result > 2147483647:
            result = 2147483647

        if result < -2147483648:
            result = -2147483648

        return result



if __name__ == '__main__':
    s = Solution()
    print(s.divide(7, -3))
