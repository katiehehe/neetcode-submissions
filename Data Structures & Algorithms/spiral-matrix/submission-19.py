class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c, direction = 0, 0, 0
        if len(matrix[0]) == 1:
            print("hi1")
            direction = 1
        dDict = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        finalList = [matrix[0][0]]
        matrix[0][0] = 101
        def canMove(r, c, direction):
            print("hi")
            if (0 <= r + dDict[direction][0] < len(matrix) and 0 <= c + dDict[direction][1] < len(matrix[0])
            and matrix[r + dDict[direction][0]][c + dDict[direction][1]] != 101):
                return True
            return False 

        while canMove(r, c, direction):
            print("hi")
            while (0 <= r + dDict[direction][0] < len(matrix) and 0 <= c + dDict[direction][1] < len(matrix[0]) 
            and matrix[r + dDict[direction][0]][c + dDict[direction][1]] != 101):
                r += dDict[direction][0]
                c += dDict[direction][1]
                finalList.append(matrix[r][c])
                matrix[r][c] = 101
            # update the direction
            direction = (direction + 1) % 4
        return finalList

                