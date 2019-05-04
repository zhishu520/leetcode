class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        # [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
        n = len(costs) / 2
        costs.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)

        A, B, DA, DB = 0, 0, 0, 0

        for i in range(0, 2*n):
            isA = costs[i][0] < costs[i][1]
            if A == n:
                B += 1
                DB += costs[i][1]
            elif B == n:
                A += 1
                DA += costs[i][0]
            elif isA:
                A += 1
                DA += costs[i][0]
            else:
                B += 1
                DB += costs[i][1]

        return DA + DB










