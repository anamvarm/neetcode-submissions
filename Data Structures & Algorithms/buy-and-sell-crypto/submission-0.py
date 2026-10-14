class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini=prices[0]
        best_profit=0

        for price in prices:
            mini=min(price,mini)
            best_profit=max(best_profit, price-mini)
        return best_profit    
            

        