

class Solution(object):

    def countAndSay(self, n):
        s = "1"
        for i in range(1, n):
            s = self.dealStr(s)
        return s

    def dealStr(self, s):
        cnt = 0
        char = s[0]

        result = ""

        for i in s:
            if i == char:
                cnt += 1
            else:
                result += str(cnt)
                result += char

                char = i
                cnt = 1

        result += str(cnt)
        result += char

        return result


if __name__ == '__main__':
    a = 10
    s = Solution()
    print(s.countAndSay(a))
