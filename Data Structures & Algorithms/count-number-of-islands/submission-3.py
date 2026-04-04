class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        q = deque()
        visit = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r,c):
            q.append((r,c))
            visit.add((r,c))

            while q:
                i, j = q.popleft()
                for dr, dc in directions:
                    row = i + dr
                    col = j + dc

                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visit:
                        q.append((row,col))
                        visit.add((row, col))
            
            return True

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(i,j)
                    res+=1
        return res