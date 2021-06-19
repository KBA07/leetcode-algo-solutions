"""
Easy

6947

216

Add to List

Share
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
Accepted
998,418
Submissions
2,037,310
"""

"""
Runtime: 28 ms, faster than 81.34% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.2 MB, less than 41.99% of Python3 online submissions for Climbing Stairs.
"""

class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:  
        if n in self.cache:
            return self.cache[n] 
        
        if n == 0:
            return 1

        if n < 0:
            return 0
        
        self.cache[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.cache[n] 

# DP
"""
Runtime: 40 ms, faster than 13.99% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.2 MB, less than 71.59% of Python3 online submissions for Climbing Stairs.
"""
class Solution:
    def climbStairs(self, n: int) -> int: 
        dp = [0, 1, 2]
        if (n==1): return dp[1]
        
        for index in range(3, n+1):
            dp.append(dp[index-1] + dp[index-2])
        
        return dp[n]

# Fibonachi as we have total number of steps fn = f(n-1) + f(n-2)
"""
Runtime: 32 ms, faster than 54.51% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.3 MB, less than 41.99% of Python3 online submissions for Climbing Stairs.
"""
class Solution:
    def climbStairs(self, n: int) -> int:  
        first = 1
        if (n==1): return first
        second = 2
        
        for _ in range(3, n+1):
            third = first + second
            first = second
            second = third
        
        return second