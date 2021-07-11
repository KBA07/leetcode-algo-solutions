"""
Medium

5642

250

Add to List

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
Accepted
676,047
Submissions
1,184,490
"""

"""
Runtime: 24 ms, faster than 96.45% of Python3 online submissions for Unique Paths.
Memory Usage: 14.4 MB, less than 14.31% of Python3 online submissions for Unique Paths.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        dp.append([1] * n)
        for _ in range(m-1):
            dp.append([1] + [0] * (n - 1)) 
        
        row_index = col_index = 0
        for row_index in range(1, m):
            for col_index in range(1, n):
                dp[row_index][col_index] = dp[row_index - 1][col_index] + dp[row_index][col_index - 1]
        
        return dp[row_index][col_index]
