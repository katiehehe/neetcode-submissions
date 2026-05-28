class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        width = n // 2
        if n % 2 == 1: 
            width += 1
        for i in range(n // 2):
            for j in range(width):
                print(f"{i} and {j}")
                dx = i - (n - 1) / 2
                dy = j - (n - 1) / 2
                tmp = matrix[i][j]
                for k in range(4):
                    dxnew = dy
                    dynew = -dx
                    tmp2 = matrix[int((n - 1) / 2 + dxnew)][int((n - 1) / 2 + dynew)]
                    matrix[int((n - 1) / 2 + dxnew)][int((n - 1) / 2 + dynew)] = tmp
                    dx = dxnew
                    dy = dynew
                    tmp = tmp2
            