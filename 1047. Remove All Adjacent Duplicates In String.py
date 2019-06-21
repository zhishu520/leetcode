class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """


        stack = []
        for i in S:

            l = len(stack)
            if l == 0 or stack[l-1] != i:
                stack.append(i)
            else:
                stack.pop()

        return "".join(stack)


