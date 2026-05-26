class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # make adjacency graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # create a visited set
        visited = set()

        def dfs(x):
            if x in visited:
                return
            visited.add(x)
            for neigh in adj[x]:
                dfs(neigh)

        count = 0
        for v in range(n):
            if v in visited:
                continue
            count += 1
            dfs(v)
        return count
            