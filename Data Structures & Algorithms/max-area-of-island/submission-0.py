class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        area = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(i,j):
            ans = 1
            q = collections.deque()
            visit.add((i,j))
            q.append((i,j))

            while q:
                row, col = q.popleft()
                directions = [(0,1), (1,0), (0,-1), (-1,0)]
                for dr, dc in directions:
                    i, j = row + dr, col + dc
                    if (i in range(rows) and j in range(cols) and grid[i][j] == 1 and (i,j) not in visit):
                        q.append((i,j))
                        visit.add((i,j))
                        ans+=1
            return ans

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    curr_area = bfs(i,j) 
                    area = max(area, curr_area)
        return area


        