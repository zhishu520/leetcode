class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == '0' or num2 == '0':
            return '0'

        l1 = list(num1)
        l2 = list(num2)

        s1 = len(l1)
        s2 = len(l2)

        rl = s1 + s2

        result = [0] * (s1 + s2)

        for i in range(0, s1):
            for j in range(0, s2):
                temp = int(l1[s1 - i - 1]) * int(l2[s2 - j - 1])
                result[i+j] += temp

        for i in range(0, rl - 1):
            result[i + 1] += result[i] / 10
            result[i] = result[i] % 10

        for i in range(0, rl):
            idx = rl - i - 1
            if result[idx] == 0:
                result.pop(idx)
            else:
                break

        rl = len(result)

        for i in range(0, rl):
            idx = rl - i - 1
            if result[idx] == 0:
                result.pop(idx)
            else:
                break

        for i in range(0, rl):
            result[i] = str(result[i])
        for i in range(0, rl/2):
            result[i], result[rl - i - 1] =  result[rl - i - 1], result[i]

        return "".join(result)






if __name__ == '__main__':
    s = Solution()
    print(s.multiply("123", "456"))
