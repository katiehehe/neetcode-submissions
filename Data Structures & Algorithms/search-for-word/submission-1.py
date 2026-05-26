class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])

        # check edge case where there isn't any expanding possible but a solution should exist
        if len(word) == 1 and r == 1 and c == 1:
            return word == board[0][0]

        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def neighbors(row, col):
            neighbor_lst = []
            for direct in directions:
                if 0 <= row + direct[0] < r and 0 <= col + direct[1] < c:
                    neighbor_lst.append((row + direct[0], col + direct[1]))
            return neighbor_lst

        def dfs(row, col, curr_len):
            print(f"DFS call at {row}, {col}, {curr_len}")
            # check if the end has been reached
            if curr_len == len(word):
                return True
            # check if visited already 
            if (row, col) in visited:
                return False
            # check if valid expansion spot
            if board[row][col] != word[curr_len]:
                return False
            # add it to the str and recurse
            visited.add((row, col))
            for neigh in neighbors(row, col):
                if dfs(neigh[0], neigh[1], curr_len + 1):
                    return True
            visited.remove((row, col))
            return False

        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    return True
        return False