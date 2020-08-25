class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        x = 0
        sidelen = len(matrix)
        while sidelen-x > 0:
            a = sidelen - x
            for i in range(x, a-1):  # swap 1. row vs right colunm
                matrix[x][i], matrix[i][a - 1] = matrix[i][a - 1], matrix[x][i]

            for i in range(x, a-1):  # swap 1. row vs last row
                matrix[x][i], matrix[a - 1][a - i-1 +x] = matrix[a - 1][a - i-1+x], matrix[x][i]

            for i in range(x, a-1):  # swap 1. row vs first column
                matrix[x][i], matrix[a - i-1+x][x] = matrix[a - i-1+x][x], matrix[x][i]

            x += 1