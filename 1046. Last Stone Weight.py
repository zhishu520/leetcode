class Solution:
    def lastStoneWeight(self, stones):
        stones.sort(reverse=True)
        while len(stones) > 1:
            r = stones[0] - stones[1]
            stones.append(r)
            del stones[0]
            del stones[0]
            stones.sort(reverse=True)
        return stones[0]