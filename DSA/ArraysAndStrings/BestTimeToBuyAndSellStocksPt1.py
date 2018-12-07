class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) < 2:
            return 0
        
        profit = 0
        minVal = prices[0]
        
        for i in range(len(prices)):

            if prices[i] < minVal:
                minVal = prices[i]
            elif (prices[i] - minVal) > profit:
                profit = prices[i] - minVal
        
        
        return profit
#test