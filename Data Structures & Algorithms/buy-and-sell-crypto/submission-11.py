class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        lowest = prices[0]

        for i in prices:
            if i < lowest:
                lowest = i
            maxprofit = max(maxprofit, i - lowest)

        return maxprofit


        
        



    

        