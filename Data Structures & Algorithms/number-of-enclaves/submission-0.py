class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def bfs(r,c):
            if r not in range(rows) or c not in range(cols) or not grid[r][c] or (r,c) in visit:
                return
            visit.add((r,c))
            for dr, dc in directions:
                bfs(r+dr, c+dc)

        for c in range(cols):
            if grid[0][c]:
                bfs(0,c)
            if grid[rows-1][c]:
                bfs(rows-1, c)
        
        for r in range(rows):
            if grid[r][0]:
                bfs(r,0)
            if grid[r][cols-1]:
                bfs(r, cols-1)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c) not in visit:
                    res+=1
        return res


