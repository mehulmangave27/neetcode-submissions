class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        dist = 0
        visit = set()

        def dfs(r,c):
            if r in range(rows) and c in range(cols) and grid[r][c] != -1 and (r,c) not in visit:
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
                dfs(r+1, c)
                dfs(r, c+1)
                dfs(r-1, c)
                dfs(r, c-1)
            dist+=1
        







        