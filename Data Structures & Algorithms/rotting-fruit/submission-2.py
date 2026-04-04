class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc

                    if (row not in range(rows) or col not in range(cols) or grid[row][col]!=1):
                        continue
                    q.append((row,col))
                    grid[row][col] = 2
                    fresh-=1
            time+=1
        
        return time if fresh == 0 else -1

