'''
[10,1,5,6,7,1]
    s     e

-if not prices return 0
-initialize start, end = first, last elements
-Intialize maxPrice = 0
-while start != end:
    -if nums[start] < nums[end]:
        -price = nums[end] - nums[start]
        -maxPrice = max(price, maxPrice)
        -increment start
    -elif nums[start] == nums[end]:
        -decrement end
    -else:
        -increment start

    -return maxPrice
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit