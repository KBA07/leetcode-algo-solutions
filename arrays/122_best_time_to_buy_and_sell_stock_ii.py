"""
Easy
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
Accepted
792,383
Submissions
1,350,274
"""

"""
Runtime: 56 ms, faster than 91.34% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15 MB, less than 89.68% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        for index in range(len(prices) - 1):
            if prices[index] < prices[index + 1]:
                    profit += prices[index + 1] - prices[index]
        
        return profit
