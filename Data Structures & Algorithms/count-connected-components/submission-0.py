class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # make adjacency graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # create a visited set
        visited = set()

        dfs_visited = set()
        def dfs(x):
            if x in dfs_visited or x in visited:
                return
            dfs_visited.add(x)
            visited.add(x)
            for neigh in adj[x]:
                dfs(neigh)
            dfs_visited.remove(x)

        count = 0
        for v in range(n):
            if v in visited:
                continue
            count += 1
            dfs(v)
        return count
            