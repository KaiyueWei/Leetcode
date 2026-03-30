class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        buyDay = 0
        res = 0
        for sellDay in range(1, n):
            sellPrice = prices[sellDay]
            buyPrice = prices[buyDay]
            if sellPrice < buyPrice:
                buyDay = sellDay
                continue
            res = max(res, sellPrice - buyPrice)
        return res


            


        