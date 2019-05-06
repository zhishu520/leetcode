
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(A)

        S = []
        s = 0
        for i in A:
            s += i
            S.append(s)

        if S[l-1] % 3 != 0:
            return False

        each = S[l-1] / 3

        left = -1
        right = -1
        for i in range(0, l):
            if S[i] == each:
                left = i
                break

        for i in range(left+1, l-1):
            if S[i] - S[left] == each:
                right = i
                break

        print(left, right)

        return left >= 0 and right > 0 and S[l-1] - S[right] == each



if __name__ == '__main__':
    s = Solution()
    r = s.canThreePartsEqualSum([12,-4,16,-5,9,-3,3,8,0])
    print(r)
