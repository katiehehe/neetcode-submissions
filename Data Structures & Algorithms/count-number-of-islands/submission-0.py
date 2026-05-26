class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "-1" or grid[i][j] == "0":
                    continue
                count += 1
                island_size = 1
                stack = [[i, j]]
                print(f"{i} and {j}")
                grid[i][j] = "-1"
                while stack:
                    loc = stack.pop()
                    for direct in direction:
                        row = loc[0] + direct[0]
                        col = loc[1] + direct[1]
                        if 0 <= row < m and 0 <= col < n and grid[row][col] == "1":
                            stack.append([row, col])
                            grid[row][col] = "-1"
                            island_size += 1
                print(island_size)
        return count

        