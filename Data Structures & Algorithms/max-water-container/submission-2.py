class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxstorage = 0

        l = 0
        r = len(heights) - 1

        while l<r:
            length = r - l
            breadth = min(heights[l], heights[r])
            storage = length * breadth
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

            maxstorage = max(storage, maxstorage)
        return maxstorage

            
        
            

        