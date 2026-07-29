class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(cur, target, visit):
            if cur == target:
                return True
            
            visit.add(cur)

            for v in adj[cur]:
                if v not in visit:
                    if dfs(v, target, visit):
                        return True
            
            return False
    
        for u, v in edges:
            visit = set()

            if adj[u] and adj[v] and dfs(u, v, visit):
                return [u, v]
            
            adj[u].append(v)
            adj[v].append(u)