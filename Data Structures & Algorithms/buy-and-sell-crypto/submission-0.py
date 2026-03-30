class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0
        sell = 1
        while buy < len(prices) and sell < len(prices):
            if prices[buy] >= prices[sell]    :
                buy = sell
                sell = sell + 1
            else:
                res = max(res, prices[sell] - prices[buy])
                sell += 1
        return res


        