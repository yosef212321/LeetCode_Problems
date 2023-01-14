class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftpt, rightpt = 0, 1
        maxProfit = 0
        while rightpt < len(prices):
            if prices[leftpt] < prices[rightpt]:
                profit = prices[rightpt] - prices[leftpt]
                maxProfit = max(maxProfit, profit)
            else:
                leftpt = rightpt
            rightpt += 1
        return maxProfit
