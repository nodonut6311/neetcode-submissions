class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visit = set()
        sol = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            size = 0
            while q:
                row, col = q.popleft()
                dirs = [[0,1],[1,0],[-1,0],[0,-1]]
                size += 1
                for dr, dc in dirs:
                    chk_row, chk_col = row + dr, col + dc

                    if(chk_row in range(rows) and chk_col in range(cols) and grid[chk_row][chk_col]== 1 and (chk_row, chk_col) not in visit):
                        visit.add((chk_row, chk_col))
                        q.append((chk_row, chk_col))
            return size
        
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == 1 and (i,j) not in visit):
                    cur_size = bfs(i, j)
                    sol = max(sol, cur_size)

        return sol

