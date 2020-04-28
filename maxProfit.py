class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        min = prices[0]
        max = prices[0]
        profit = max - min

        for i in range(0, len(prices)):
            if prices[i] < min:
                max = min = prices[i]
            if prices[i] > max:
                max = prices[i]

            if profit < (max - min):
                profit = max - min

        return profit