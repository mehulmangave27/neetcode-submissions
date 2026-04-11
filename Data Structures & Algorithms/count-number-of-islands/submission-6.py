class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        res = 0

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def dfs(i,j):
            q.append((i,j))
            visit.add((i,j))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc

                    if (row, col) not in visit and row in range(rows) and col in range(cols) and grid[row][col] == "1":
                        visit.add((row,col))
                        q.append((row, col))
            return
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    dfs(r,c)
                    res+=1
        
        return res

        
        