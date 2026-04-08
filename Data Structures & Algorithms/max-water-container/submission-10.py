class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxstorage = 0
        l, r = 0, len(heights)-1

        while l <= r:
            storage = min(heights[l], heights[r]) * (r-l)
            maxstorage = max(storage, maxstorage)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return maxstorage


            


            
        
            

        