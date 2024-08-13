# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.from typing import List
#

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
            # Calculate the potential profit
            profit = price - min_price
            # Update the maximum profit
            max_profit = max(max_profit, profit)

        return max_profit