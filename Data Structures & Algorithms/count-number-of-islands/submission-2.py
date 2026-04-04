class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        q = deque()
        visit = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(r, c):
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    islands+=1

        return islands
