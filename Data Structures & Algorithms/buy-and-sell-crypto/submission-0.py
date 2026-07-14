class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        use two pointers for this problem
        we want to make sure the buy point is the lowest
        record the max_profit
        if we find a lower buy point, left pointer moves to this lowest buy point, and calculate the max_point
        make comparison, and return the final max_profit
        '''

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                new_profit = prices[right] - prices[left]
                max_profit = max(max_profit, new_profit)
            
            right += 1
        
        return max_profit
