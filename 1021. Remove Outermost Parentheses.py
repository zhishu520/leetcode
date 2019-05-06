class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """

        stack = []
        r = ""

        for i in S:
            if i == "(":
                if len(stack) > 0:
                    r += "("
                stack.append(i)
            else:
                stack.pop()
                if len(stack) > 0:
                    r += ")"

        print(r)
        return r

if __name__ == '__main__':
    s = Solution()
    s.removeOuterParentheses("(()())")
