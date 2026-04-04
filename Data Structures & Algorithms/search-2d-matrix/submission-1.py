class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows-1

        while top <= bot:
            mid = (top + bot)//2

            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bot = mid -1
            else:
                break
         
        if not(top<=bot):
            return False
        
        row = mid

        l, r = 0, cols-1

        while l <= r:
            m = (l+r)//2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m+1
        return False 

        