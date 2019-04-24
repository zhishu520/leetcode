class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    # '(', ')', '{', '}', '[' and ']'

        stack = []
        for i in s:
            if i == '(' or i == '{' or i == "[":
                stack.append(i)
            else:
                l = len(stack)
                if l == 0:
                    return False

                if stack[l-1] == "(" and i == ")":
                    stack.pop()
                elif stack[l-1] == "[" and i == "]":
                    stack.pop()
                elif stack[l-1] == "{" and i == "}":
                    stack.pop()
                else:
                    stack.append(i)

        return len(stack) == 0



if __name__ == '__main__':
    s = Solution()
    print(s.isValid("{"))
