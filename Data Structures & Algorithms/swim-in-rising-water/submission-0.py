class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        visit = set()
        heap = [[grid[0][0], 0, 0]]
        visit.add((0,0))

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == N-1 and c == N-1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr not in range(N) or nc not in range(N) or (nr, nc) in visit):
                    continue
                visit.add((nr, nc))
                heapq.heappush(heap, [max(t, grid[nr][nc]), nr, nc])

