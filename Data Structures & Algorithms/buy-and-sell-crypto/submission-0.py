class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1 ##Left= buying, Right= selling ##Two pointer (Sliding window) --> SP(O(n)), TC(O(1))
        maxprofit=0

        while right < len(prices): #checking right is end of prices
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit) #assign to the new max point 
            else:  #Buying here
                left = right  ##buy low sell high 
            right += 1
        return maxprofit