"""
322. Coin Change
Medium

7558

207

Add to List

Share
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
Accepted
690,242
Submissions
1,801,234
"""

"""
Runtime: 1624 ms, faster than 37.97% of Python3 online submissions for Coin Change.
Memory Usage: 14.3 MB, less than 92.79% of Python3 online submissions for Coin Change.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for index in range(len(dp)):
            for coin in coins:
                if coin <= index: # coins can be added as denomination
                    dp[index] = min(dp[index], 1 + dp[index - coin])  # 1 coin + total number of coins which was at amount - coin
        
        return -1 if dp[amount] > amount else dp[amount]
