from typing import List
# time: O(n)
# space: 0(1)
# mine
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0

        while r < len(prices):
            # + profit
            if prices[r] > prices[l]: max_profit = max(max_profit, prices[r] - prices[l])
            # - or = profit
            else: l = r
            r += 1
        return max_profit
# other's
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if p < buy_price:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit