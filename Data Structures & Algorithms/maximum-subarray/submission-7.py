class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = max(nums)
        l, r = 0,1
        cur_sum = nums[l]

        while r < len(nums):
            cur_sum+=nums[r]

            if cur_sum <= 0:
                l = r
                r = r+1
                cur_sum = 0
            else:
                max_sub = max(cur_sum, max_sub)
                r+=1

        return max_sub

            

        