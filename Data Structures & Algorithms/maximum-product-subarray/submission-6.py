class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = 1
        curmin = 1
        res = max(nums)
        for i in nums:
            temp = curmax
            curmax = max(curmax*i, curmin*i, i)
            curmin = min(curmin*i, temp*i, i)
            res = max(curmax, res)
        return res


        
        