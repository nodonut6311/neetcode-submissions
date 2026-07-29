class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(cur, parent):
            if cur in visit:
                return False

            visit.add(cur)

            for v in adj[cur]:
                if v == parent:
                    continue
                if not dfs(v, cur):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n