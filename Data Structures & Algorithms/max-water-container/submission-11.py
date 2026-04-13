class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxstorage = 0

        while l <= r:
            if heights[l] < heights[r]:
                storage = (r-l)*heights[l]
                maxstorage = max(storage, maxstorage)
                l+=1
            
            else:
                storage = (r-l)*heights[r]
                maxstorage = max(storage, maxstorage)
                r-=1
        
        return maxstorage
        


            


            
        
            

        