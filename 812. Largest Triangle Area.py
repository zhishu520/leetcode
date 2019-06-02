def calc_area(p1, p2, p3):
    x1 = p1[0]
    x2 = p2[0]
    x3 = p3[0]

    y1 = p1[1]
    y2 = p2[1]
    y3 = p3[1]

    return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        l = len(points)

        max = 0
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):

                    a = calc_area(points[i], points[j], points[k])
                    if max < a:
                        max = a
        return max








