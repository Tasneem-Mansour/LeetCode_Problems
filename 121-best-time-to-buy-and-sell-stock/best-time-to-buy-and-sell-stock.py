import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyMin  = prices[0]           #7
        profit = 0                   
        
        for i in range(1, len(prices)):
            if prices[i] < buyMin:
                buyMin = prices[i]

            profit = max(profit, prices[i]-buyMin)


        return profit  