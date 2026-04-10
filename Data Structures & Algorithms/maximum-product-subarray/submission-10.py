class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin = 1
        curmax = 1
        res = max(nums)

        for i in nums:
            temp = curmax
            curmax = max(i*curmax, i, i*curmin)
            curmin = min(i, temp*i, curmin*i)
            res = max(curmax, res)

        return res


        
        