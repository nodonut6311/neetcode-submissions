class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n

        res = [[0] * (n+1) for i in range(m+1)]
        res[rows-1][cols] = 1

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                res[r][c] = res[r+1][c] + res[r][c+1]

        return res[0][0]