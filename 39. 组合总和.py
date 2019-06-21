class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        l = len(candidates)

        def isearch(start, target, arr):
            if target == candidates[start]:
                arr.append(candidates[start])
                ret.append(arr)
            elif target > candidates[start]:
                if start + 1 < l:
                    isearch(start + 1, target, arr[::])

                t1 = arr[::]
                t1.append(candidates[start])
                isearch(start, target - candidates[start], t1)

        isearch(0, target, [])
        return ret
