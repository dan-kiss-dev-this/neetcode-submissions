class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # how to solve, find the current price and biggest difference
        # just run off the video
        # coordinate system? x is day, y is value?

        # two pointer left day1, right on day2
        l, r = 0, 1
        #left is buy, right is sell
        maxP = 0

        while r< len(prices):
            # profitable
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+=1

        return maxP

        