
class Solution(object):

    def permuteUnique(self, nums):
        ret = []
        self.permute_one(nums, [], ret)
        return ret

    def permute_one(self, pool, cur, ret):
        if len(pool) == 0 and not ret.__contains__(cur):
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
    s = Solution()
    a = [1,1,2]
    print(s.permuteUnique(a))