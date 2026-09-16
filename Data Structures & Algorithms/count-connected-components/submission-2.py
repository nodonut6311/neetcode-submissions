class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        res = 0
        def dfs(cur, visit, adj):
            visit.add(cur)
            for v in adj[cur]:
                if v not in visit:
                    dfs(v, visit, adj)
        
        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i, visit, adj)

        return res
                