class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time = 0
        fresh = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append((i,j))
        

        while fresh>0 and q:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh-=1
                        q.append((r,c))
            time+=1
        return time if fresh == 0 else -1
                

