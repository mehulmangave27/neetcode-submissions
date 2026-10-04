class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        visit = set()
        islands = 0

        rows,cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(i,j):
            visit.add((i,j))
            q.append((i,j))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r,c = row+dr, col+dc

                    if (r,c) not in visit and r in range(rows) and c in range(cols) and grid[r][c]=="1":
                        visit.add((r,c))
                        q.append((r,c))

            return 

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    dfs(r,c)
                    islands+=1

        return islands


        

        
        