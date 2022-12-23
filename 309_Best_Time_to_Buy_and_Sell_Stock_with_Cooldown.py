class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:        
            pre_sold = sold     # pre_sold servers as sold[i - 1]
            sold = held + price     # sold servers as sold[i]
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)
