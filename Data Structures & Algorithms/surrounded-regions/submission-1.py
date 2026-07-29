class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        vis = [[0] * cols for _ in range(rows)]

        def dfs(r, c, board, vis):
            vis[r][c] = 1
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and board[nr][nc] == "O" and not vis[nr][nc]:
                    dfs(nr, nc, board, vis)

        for j in range(cols):
            if board[0][j] == "O" and not vis[0][j]:
                dfs(0, j, board, vis)
            if board[rows - 1][j] == "O" and not vis[rows - 1][j]:
                dfs(rows - 1, j, board, vis)

        for k in range(rows):
            if board[k][0] == "O" and not vis[k][0]:
                dfs(k, 0, board, vis)
            if board[k][cols - 1] == "O" and not vis[k][cols - 1]:
                dfs(k, cols - 1, board, vis)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and vis[r][c] == 0:
                    board[r][c] = "X"