class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for pair in prerequisites:
            adj.setdefault(pair[1], set()).add(pair[0])
        visited = set()
        print(adj)
        for i in range(numCourses):
            if i in visited:
                continue
            visited.add(i)
            stack = [i]
            visited_dfs = {i}
            while stack:
                top = stack.pop(-1)
                for neighbor in adj.get(top, []):
                    if neighbor in visited_dfs:
                        return False
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited_dfs.add(neighbor)
                        visited.add(neighbor)
        return True