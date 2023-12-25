class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftptr = 0
        rightptr = 1
        maxProfit = -500

        while rightptr < len(prices):
            profit = prices[rightptr] - prices[leftptr]
            if profit > maxProfit:
                maxProfit = profit
            if prices[rightptr] < prices[leftptr]:
                leftptr = rightptr    
            rightptr += 1

        if maxProfit > 0:
            return maxProfit
        else:
            return 0