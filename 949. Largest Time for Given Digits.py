class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        max = 0

        for i in range(24):
            if A[0] * 10 + A[1] >= 24 or A[2] * 10 + A[3] >= 60:
                self.nextPermutation(A)
                continue

            if max == 0 or A[0] * 60 * 10 + A[1] * 60 + A[2] * 10 + A[3] > max[0] * 60 * 10 + max[1] * 60 + max[2] * 10 + max[3]:
                print(A)
                max = A[::]

            self.nextPermutation(A)
            print A

        if max == 0:
            return ""
        else:
            return str(max[0]) + str(max[1]) + ":" + str(max[2]) + str(max[3])


    def nextPermutation(self, nums):
        size = len(nums)
        ti = size - 2

        while ti >= 0:
            if nums[ti] < nums[ti+1]:
                break
            ti -= 1

        if ti >= 0:
            ni = size - 1
            while ni > ti:
                if nums[ni] > nums[ti]:
                    break
                ni -= 1

            nums[ti], nums[ni] = nums[ni], nums[ti]

            half = (size - 1 - ti) / 2
            for i in range(0, half):
                nums[ti + i + 1], nums[size - 1 - i] = nums[size - 1 - i], nums[ti + i + 1]
        else:
            half = size / 2
            for i in range(0, half):
                nums[i], nums[size - 1 - i] = nums[size - 1 - i], nums[i]

if __name__ == '__main__':
    s = Solution()
    r = s.largestTimeFromDigits([4,1,0,0])
    print(r)