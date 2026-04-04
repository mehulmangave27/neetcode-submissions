class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        res = 0

        for i in prices:
            if i < low:
                low = i
            res = max(res, i - low)
        return res
        



    

        