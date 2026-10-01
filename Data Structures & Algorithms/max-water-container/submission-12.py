class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxstorage = 0

        while l < r:
            storage = min(heights[l], heights[r]) * (r-l)

            maxstorage = max(storage, maxstorage)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return maxstorage
                