class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        hold = -prices[0] # bought stock
        sold = 0 # sold today (impossible on day 0, but treat as 0)
        rest = 0 # not holding, free to buy

        for price in prices[1:]:
            prev_hold = hold 
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest-price)  # If we end today holding: either keep holding, or buy today from rest
            sold = prev_hold + price # If we end today just sold: must have been holding yesterday and sell
            # If we end today resting: either we were already resting, or we just finished cooldown from selling yesterday
            rest = max(prev_rest,prev_sold) 
        # At the end, best profit is when not holding stock
        return max(sold, rest)