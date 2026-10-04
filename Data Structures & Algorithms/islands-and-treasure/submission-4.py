class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        dist = 0

        def bfs(r,c):
            if 0<=r<rows and 0<=c<cols and (r,c) not in visit and grid[r][c]!=-1:
                q.append((r,c))
                visit.add((r,c))
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                for dr,dc in directions:
                    row, col = dr+r, dc+c
                    bfs(row,col)
            dist+=1
        





        