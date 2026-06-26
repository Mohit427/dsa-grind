class Solution(object):
    def maxProfit(self, prices):
        min_price=prices[0]
        best_profit=0
        for i in range(1,len(prices)):
            min_price=min(min_price, prices[i])
            best_profit=max(best_profit,prices[i]-min_price)
            
        return best_profit

            

