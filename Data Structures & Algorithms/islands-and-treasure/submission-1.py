class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        dist = 0
        q = deque()

        def addroom(r,c):
            if (r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append((r,c))



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    q.append((i,j))
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addroom(r+1, c)
                addroom(r, c+1)
                addroom(r-1, c)
                addroom(r, c-1)
            dist+=1



        