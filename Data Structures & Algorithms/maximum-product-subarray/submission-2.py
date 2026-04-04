class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmax, curmin = 1, 1
        for i in nums:
            temp = curmax
            curmax = max(curmax*i, curmin*i, i)
            curmin = min(temp*i, curmin*i, i)
            res = max(res, curmax)
        return res
        
        