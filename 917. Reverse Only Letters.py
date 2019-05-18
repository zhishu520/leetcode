class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        s = len(S)

        S = list(S)

        l, r = 0, len(S)-1

        while l < r:
            while l < s and not S[l].isalpha():
                print("yes 1")
                l += 1

            while r >= 0 and not S[r].isalpha():
                print("yes 2")
                r -= 1

            if l >= r:
                break
            print("yes 3")

            S[l], S[r] = S[r], S[l]

            l += 1
            r -= 1

        return "".join(S)

if __name__ == '__main__':
    s = Solution()
    print s.reverseOnlyLetters("?6C40E")



