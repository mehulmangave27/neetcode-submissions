class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = 1
        curmin = 1
        res = max(nums)

        for i in nums:
            temp = curmax
            curmax = max(i, curmax*i, curmin*i)
            curmin = min(i, temp*i, curmin*i)
            res = max(curmax, res)
        return res