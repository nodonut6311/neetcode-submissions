class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        vis = [[0] * cols for _ in range(rows)]

        q = deque()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    vis[r][c] = 1

        while q:
            r, c, d = q.popleft()
            grid[r][c] = d

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and not vis[nr][nc] and grid[nr][nc] == INF:
                    vis[nr][nc] = 1
                    q.append((nr, nc, d + 1))