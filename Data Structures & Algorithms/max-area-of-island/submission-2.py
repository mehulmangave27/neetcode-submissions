class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        row = len(grid)
        col = len(grid[0])
        visit = set()
        q = deque()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(r,c):
            visit.add((r,c))
            q.append((r,c))
            area = 1

            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    rows = r + dr
                    cols = c + dc

                    if rows in range(row) and cols in range(col) and grid[rows][cols] == 1 and (rows, cols) not in visit:
                        area+=1
                        q.append((rows, cols))
                        visit.add((rows, cols))
            return area
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visit:
                    area = bfs(i,j)
                    max_area = max(area, max_area)
        return max_area
        