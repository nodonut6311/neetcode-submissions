class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        while q:
            r, c, t = q.popleft()
            time = t

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))
        
        return time if fresh == 0 else -1