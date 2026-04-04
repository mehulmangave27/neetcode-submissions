class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        max_area = 0
        area = 0
        q = deque()

        def bfs(r,c):
            area = 1
            visit.add((r,c))
            q.append((r,c))
            directions = [(0,1), (1,0), (0,-1), (-1,0)]

            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        area+=1
            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
        return max_area



        