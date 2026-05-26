class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check the number of edges
        if len(edges) != n - 1:
            return False
        # create adjacency graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # check connectedness, starting at 0
        agenda = [0]
        visited = {0}
        while agenda:
            last = agenda.pop(-1)
            for neighbor in adj[last]:
                if neighbor in visited:
                    continue
                agenda.append(neighbor)
                visited.add(neighbor)
        if len(visited) != n:
            return False
        return True