class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) time ad O(1) space
        # profit = 0
        # for i in range(len(prices)-1):
        #     b = i
        #     s = i+1
        #     if prices[s] > prices[b]:
        #         profit += prices[s] - prices[b]
        # return profit

        # O(n) time ad O(1) space
        profit = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit
            