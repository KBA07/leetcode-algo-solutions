"""
62. Unique Paths
Medium

5646

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
676,404
Submissions
1,184,977
"""

"""
Runtime: 32 ms, faster than 66.24% of Python3 online submissions for Unique Paths.
Memory Usage: 14.3 MB, less than 37.18% of Python3 online submissions for Unique Paths.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.cache = {}
        unique_paths = 0
        self.m = m
        self.n = n

        unique_paths += self.dfs(0, 0, m, n)
        
        return unique_paths
        
    
    def dfs(self, row, col, m, n):
        if row < 0 or row > m - 1 or col < 0 or col > n - 1: return 0
            
        key = f"{row}:{col}"
        if key in self.cache: return self.cache[key]
        
        if row == m - 1 and col == n - 1: return 1
        
        val1 = self.dfs(row + 1, col, m, n)
        self.cache[f"{row + 1}:{col}"] = val1
        
        val2 = self.dfs(row, col + 1, m, n)
        self.cache[f"{row}:{col + 1}"] = val2
        
        return val1 + val2
