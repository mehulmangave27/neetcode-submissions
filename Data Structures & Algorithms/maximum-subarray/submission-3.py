class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        res = 0

        for n in nums:
            if res < 0:
                res = 0
            res+=n
            maxsub = max(maxsub, res)
        
        return maxsub
        