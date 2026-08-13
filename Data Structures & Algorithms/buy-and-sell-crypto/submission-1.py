class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##Greedy algo TC(O(n)), SP(O(1))
        min_price=float('inf') #example of this step :1st step --> min(infinity, 7) = 7,min(7, 1) = 1 then  
        max_profit = 0

        for price in prices:
            min_price = min(min_price,price)
            max_profit = max(max_profit,price-min_price)
        return max_profit