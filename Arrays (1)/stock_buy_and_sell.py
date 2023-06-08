from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrices = 10**5
        maxProfit = 0
        for price in prices:
            minPrices = min(minPrices,price)
            maxProfit = max(maxProfit,price-minPrices)
        return maxProfit

# Time Complexity: O(n)
# Space Complexity: O(1)