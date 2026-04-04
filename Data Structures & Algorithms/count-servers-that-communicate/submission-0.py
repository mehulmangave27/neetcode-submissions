class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        rows_count = [0]*rows
        cols_count = [0]*cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rows_count[i]+=1
                    cols_count[j]+=1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (rows_count[i] > 1 or cols_count[j] > 1):
                    res+=1
        
        return res
        