class Solution:
    def maxArea(self, heights: List[int]) -> int:
        storage = []
        distance = 0
        height = 0

        l, r = 0, len(heights)-1

        while l<r:
            height = min(heights[l],heights[r])
            distance = r-l

            storage.append(height*distance)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max(storage)
            


            
        
            

        