class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([(0,0,1)])
        visit = set([0,0])
        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1, -1)]

        while q:
            r,c,length = q.popleft()
            if (r not in range(n) or c not in range(n) or grid[r][c]==1):
                continue

            if r==n-1 and c==n-1:
                return length

            for dr, dc in directions:
                if ((r+dr, c+dc) not in visit):
                    q.append((r+dr, c+dc, length+1))
                    visit.add((r+dr, c+dc))

        return -1

            


