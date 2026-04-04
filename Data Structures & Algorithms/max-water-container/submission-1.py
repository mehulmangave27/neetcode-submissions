class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1

        maxstored = 0

        while l<r:
            stored = (r-l)*min(heights[r],heights[l])
            maxstored = max(stored , maxstored)

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        
        return maxstored
            

        