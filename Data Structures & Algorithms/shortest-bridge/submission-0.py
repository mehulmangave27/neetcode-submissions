class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        res = 0
        visit = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r,c):
            if r not in range(N) or c not in range(N) or (r,c) in visit or grid[r][c] == 0:
                return
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        curR, curC = r+dr, c+dc
                        if curR not in range(N) or curC not in range(N) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append((curR, curC))
                        visit.add((curR, curC))
                res+=1


        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()
                    