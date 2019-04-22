class Solution(object):
    def rotate(self, matrix):
        result = []
        size = len(matrix)

        for i in range(0, size):
            line = []
            for j in range(0, size):
                line.append(matrix[i][j])
            result.append(line)
        print(result)

        for i in range(0, size):
            for j in range(0, size):
                matrix[i][j] = result[size-1-j][i]


if __name__ == '__main__':
    s = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix)
    print(matrix)
