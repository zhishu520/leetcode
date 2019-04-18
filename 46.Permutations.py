




'''
    1234
    1243
    1324
    2134
'''


class Solution(object):

    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def permute(self, nums):
        ret = []
        self.permute_one(nums, [], ret)
        return ret

    def permute_one(self, pool, cur, ret):
        if len(pool) == 0:
            ret.append(cur)
            return

        size = len(pool)

        for i in range(0, size):
            newcur = cur[:]
            newcur.append(pool[i])

            newpool = pool[:]
            newpool.pop(i)

            self.permute_one(newpool, newcur, ret)









if __name__ == '__main__':
    a = [1,2,3,4]
    s = Solution()
    print(s.permute(a))


    # a = [[5,4,6,2],[5,6,4,2],[6,5,4,2],[6,5,2,4],[6,2,5,4],[2,6,5,4],[2,6,4,5],[2,4,6,5],[4,2,6,5],[4,2,5,6],[4,5,2,6],[5,4,2,6],[5,4,6,2],[5,6,4,2],[6,5,4,2],[6,5,2,4],[6,2,5,4],[2,6,5,4],[2,6,4,5],[2,4,6,5],[4,2,6,5],[4,2,5,6],[4,5,2,6],[5,4,2,6]]
    # b = [[5,4,6,2],[5,4,2,6],[5,6,4,2],[5,6,2,4],[5,2,4,6],[5,2,6,4],[4,5,6,2],[4,5,2,6],[4,6,5,2],[4,6,2,5],[4,2,5,6],[4,2,6,5],[6,5,4,2],[6,5,2,4],[6,4,5,2],[6,4,2,5],[6,2,5,4],[6,2,4,5],[2,5,4,6],[2,5,6,4],[2,4,5,6],[2,4,6,5],[2,6,5,4],[2,6,4,5]]
    #
    # for i in a:
    #     print(b.index(i))

