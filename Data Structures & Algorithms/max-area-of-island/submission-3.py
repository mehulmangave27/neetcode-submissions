class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        q = deque()
        visit = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q.append((r,c))
            visit.add((r,c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r,c) not in visit):
                        area+=1
                        q.append((r,c))
                        visit.add((r,c))
            return area
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visit:
                    area = bfs(i,j)
                    max_area = max(area, max_area)
        return max_area




        