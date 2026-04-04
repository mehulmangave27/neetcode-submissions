class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]

        if orig == color:
            return image
        
        m, n = len(image), len(image[0])

        q = deque([(sr,sc)])
        image[sr][sc] = color
        directions = [(1,0), (0,1), (0, -1), (-1,0)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<= nr < m and 0<= nc <n and image[nr][nc] == orig:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image