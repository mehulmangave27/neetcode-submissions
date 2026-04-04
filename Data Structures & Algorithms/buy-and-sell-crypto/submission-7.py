class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        res = 0

        for i in range(0, len(prices)):
            if prices[i]<low:
                low = prices[i]
            res = max(res,prices[i] - low)
        return res 

        
        



    

        