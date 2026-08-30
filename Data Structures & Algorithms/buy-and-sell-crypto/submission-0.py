class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # brute force
        # max_profit = 0
        # n = len(prices)
        # for i in range(n-1):
        #     j = i+1
        #     for j in range(i+1, n):
        #         max_profit = max(max_profit, (prices[j] - prices[i]))
        
        # return max_profit

        # optimal way
        max_profit = 0 
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
