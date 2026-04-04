class Solution:
    def maxArea(self, heights: List[int]) -> int:
        storage = 0
        l, r = 0, len(heights)-1
        

        while l < r:
            curstorage = (r-l)*min(heights[l], heights[r])
            storage = max(storage, curstorage)

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return storage

            


            
        
            

        