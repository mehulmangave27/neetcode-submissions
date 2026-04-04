class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = 1
        maxstored = 0

        for i in range (0,len(heights)):
            for j in range (i,len(heights)):
                stored = min(heights[i],heights[j])*(j - i)
                maxstored = max(stored, maxstored)
        return maxstored   
            

        