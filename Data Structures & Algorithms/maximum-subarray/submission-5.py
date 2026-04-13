class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = max(nums)
        l, r = 0, 1
        total = nums[l]

        while r < len(nums):
            total += nums[r]

            if total <= 0:
                l = r
                r = r+1
                total = 0
            else:
                r+=1
                max_sub = max(max_sub, total)
        return max_sub

        
        