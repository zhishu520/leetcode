class Solution(object):
    def rob(self, nums):

        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]

        m = nums[0] if nums[0] > nums[1] else nums[1]
        arr = [nums[0], m]

        for i in range(2, l):
            a = nums[i] + arr[i-2]
            b = arr[i-1]
            arr.append(a if a > b else b)
            print("ab", a, b)

        print(arr)
        return arr[l-1] if arr[l-1] > arr[l-2] else arr[l-2]

if __name__ == '__main__':
    s = Solution()
    arr = [2, 1, 1, 2]
    print(s.rob(arr))