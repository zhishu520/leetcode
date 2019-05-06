class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        l = len(A)

        if l < 3:
            return False

        flag = True

        for i in range(l - 1):
            if flag:
                if A[i + 1] < A[i]:
                    if i == 0:
                        return False
                    else:
                        flag = False
            else:
                if A[i + 1] >= A[i]:
                    return False

        return True if flag == False else False


if __name__ == '__main__':
    s = Solution()
    r = s.validMountainArray([0,3,2,1])
    print r


