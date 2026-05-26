class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        r, c = len(heights), len(heights[0])
        pacific = [[0] * c for _ in range(r)]
        atlantic = [[0] * c for _ in range(r)]
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(ocean, stack, visited):
            while stack:
                x, y = stack.pop()
                for dx, dy in direct:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < r and 0 <= ny < c and
                        heights[nx][ny] >= heights[x][y] and
                        (nx, ny) not in visited):
                        visited.add((nx, ny))
                        ocean[nx][ny] = 1
                        stack.append((nx, ny))

        # Initialize Pacific
        pacific_stack = []
        pacific_visited = set()
        for i in range(r):
            pacific_stack.append((i, 0))
            pacific_visited.add((i, 0))
            pacific[i][0] = 1
        for j in range(c):
            pacific_stack.append((0, j))
            pacific_visited.add((0, j))
            pacific[0][j] = 1

        # Initialize Atlantic
        atlantic_stack = []
        atlantic_visited = set()
        for i in range(r):
            atlantic_stack.append((i, c - 1))
            atlantic_visited.add((i, c - 1))
            atlantic[i][c - 1] = 1
        for j in range(c):
            atlantic_stack.append((r - 1, j))
            atlantic_visited.add((r - 1, j))
            atlantic[r - 1][j] = 1

        # Run DFS
        dfs(pacific, pacific_stack, pacific_visited)
        dfs(atlantic, atlantic_stack, atlantic_visited)

        # Collect cells reachable by both oceans
        final_arr = []
        for i in range(r):
            for j in range(c):
                if pacific[i][j] and atlantic[i][j]:
                    final_arr.append([i, j])

        return final_arr
