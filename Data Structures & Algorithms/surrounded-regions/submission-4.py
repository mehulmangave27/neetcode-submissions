class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def search(r,c):
            if r not in range(rows) or c not in range(cols) or board[r][c]!= "O":
                return
            board[r][c] = "#"
            search(r+1, c)
            search(r, c+1)
            search(r-1, c)
            search(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0,rows-1] or c in [0, cols-1]):
                    search(r,c)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"