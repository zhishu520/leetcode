
class Solution(object):

    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def permute(self, nums):
        r = []
        size = len(nums)

        cnt = 1
        for i in range(1, size + 1):
            cnt = cnt * i

        last = nums
        r.append(last)

        for i in range(1, cnt):
            last = self.permute_one(last, size, i)
            r.append(last)

        return r


    def permute_one(self, nums, size, i):
        i1 = i % (size - 1) + 1
        i2 = size - i1
        i = i2

        arr = nums[:]
        temp = arr[i - 1]
        arr[i - 1] = arr[i]
        arr[i] = temp
        return arr


if __name__ == '__main__':
    # a = [1,2,3,4]
    # s = Solution()
    # print(s.permute(a))
    a = [[5,4,6,2],[5,6,4,2],[6,5,4,2],[6,5,2,4],[6,2,5,4],[2,6,5,4],[2,6,4,5],[2,4,6,5],[4,2,6,5],[4,2,5,6],[4,5,2,6],[5,4,2,6],[5,4,6,2],[5,6,4,2],[6,5,4,2],[6,5,2,4],[6,2,5,4],[2,6,5,4],[2,6,4,5],[2,4,6,5],[4,2,6,5],[4,2,5,6],[4,5,2,6],[5,4,2,6]]
    b = [[5,4,6,2],[5,4,2,6],[5,6,4,2],[5,6,2,4],[5,2,4,6],[5,2,6,4],[4,5,6,2],[4,5,2,6],[4,6,5,2],[4,6,2,5],[4,2,5,6],[4,2,6,5],[6,5,4,2],[6,5,2,4],[6,4,5,2],[6,4,2,5],[6,2,5,4],[6,2,4,5],[2,5,4,6],[2,5,6,4],[2,4,5,6],[2,4,6,5],[2,6,5,4],[2,6,4,5]]

    for i in a:
        print(b.index(i))

