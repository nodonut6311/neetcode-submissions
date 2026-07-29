class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, visit, prevHt):
            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and heights[nr][nc] >= prevHt:
                    dfs(nr, nc, visit, heights[nr][nc])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r,c))
        
        return res
