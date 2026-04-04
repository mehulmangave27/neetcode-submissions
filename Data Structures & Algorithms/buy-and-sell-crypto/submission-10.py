class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        res = 0

        for n in prices:
            if n<low:
                low = n
            res = max(res, n-low)
        return res

        
        



    

        