class Solution(object):
    def search(self, nums, target):

        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        s = len(nums)
        l, r = 0, len(nums) - 1
        t = -1
        while l <= r:
            m = (l + r) / 2

            if nums[m] > nums[m+1]:
                t = m
                break
            elif nums[m-1] > nums[m]:
                t = m - 1
                break
            elif nums[m] < nums[l]:
                r = m - 1
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                break

        if t == -1:
            return self.bs(nums, 0, s-1, target)
        else:
            if target < nums[0]:
                return self.bs(nums, t+1, s-1, target)
            else:
                return self.bs(nums, 0, t, target)



    def bs(self, nums, l, r, target):
        if l > r:
            return -1

        m = (l + r) / 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.bs(nums, l, m - 1, target)
        else:
            return self.bs(nums, m + 1, r, target)



if __name__ == '__main__':
    s = Solution()
    arr = [6,7,8,1,2,3,4,5]
    print(s.search(arr, 6))
