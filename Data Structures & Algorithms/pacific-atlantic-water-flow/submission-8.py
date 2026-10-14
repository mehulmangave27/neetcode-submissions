class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visit, adjheight):
            if (0<=r<rows and 0<=c<cols and (r,c) not in visit and heights[r][c]>=adjheight):
                visit.add((r,c))
                dfs(r+1, c, visit, heights[r][c])
                dfs(r, c+1, visit, heights[r][c])
                dfs(r, c-1, visit, heights[r][c])
                dfs(r-1, c, visit, heights[r][c])

        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])

        res = []
        for (r,c) in pacific:
            if (r,c) in atlantic:
                res.append([r,c])

        return res
        