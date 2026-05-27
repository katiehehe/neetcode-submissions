class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        # keep track of the 1st row
        row0 = 1
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = 0
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # go through the array again and set entries to 0
        # inner matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 1st column
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        # 1st row
        if row0 == 0:
            for j in range(n):
                matrix[0][j] = 0