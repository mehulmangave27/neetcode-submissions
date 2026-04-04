class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        q = deque()
        visit = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r,c):
            area = 1
            q.append((r,c))
            visit.add((r,c))

            while q:
                i, j = q.popleft()
                for dr, dc in directions:
                    row = i + dr
                    col = j + dc

                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row, col) not in visit:
                        q.append((row,col))
                        visit.add((row, col))
                        area+=1
            
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    res = max(res, dfs(i,j))

        return res