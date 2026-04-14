class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        q = deque()
        visit = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r,c):
            if (r,c) in visit:
                return 0
            q.append((r,c))
            visit.add((r,c))
            area = 1

            while q:
                i, j = q.popleft()
                for dr, dc in directions:
                    row, col = i + dr, j + dc

                    if row in range(rows) and col in range(cols) and (row, col) not in visit and grid[row][col] == 1:
                        area+=1
                        q.append((row, col))
                        visit.add((row, col))
                    else:
                        continue
            
            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))

        return max_area
        
        