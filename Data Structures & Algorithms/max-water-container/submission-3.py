class Solution:
    def maxArea(self, heights: List[int]) -> int:
        storage = 0
        distance = 0

        l,r = 0,len(heights)-1
        while l<r:
            distance = r - l
            ht = min(heights[l],heights[r])
            wat = distance*ht
            storage = max(wat,storage)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return storage


            
        
            

        