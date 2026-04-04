class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        islands = 0
        visit = set()
        directions = [(1,0), (0,1), (-1,0), [0,-1]]

        def search(r,c):
            queue.append((r,c))
            visit.add((r,c))
            while queue:
                ROW, COL = queue.popleft()
                for dr,dc in directions:
                    row = dr + ROW
                    col = dc + COL

                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row,col) not in visit:
                        queue.append((row, col))
                        visit.add((row, col))
            return True



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and ((r,c)) not in visit:
                    search(r,c)
                    islands+=1
        
        return islands