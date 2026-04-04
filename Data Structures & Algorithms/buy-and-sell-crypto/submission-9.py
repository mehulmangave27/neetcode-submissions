class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]

        for i in prices:
            if i < low:
                low = i
            res = max(res, i - low)
        return res
        