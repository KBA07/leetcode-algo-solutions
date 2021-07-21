"""
221. Maximal Square
Medium

5034

116

Add to List

Share
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
Accepted
377,640
Submissions
933,261
"""

"""
Runtime: 220 ms, faster than 51.24% of Python3 online submissions for Maximal Square.
Memory Usage: 15.9 MB, less than 15.81% of Python3 online submissions for Maximal Square.
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        for _ in range (len(matrix) + 1):
            dp.append(([0] * (len(matrix[0]) + 1))) 
        
        max_area = 0
        for row in range(1, len(matrix) + 1):
            for col in range(1, len(matrix[0]) + 1):
                if matrix[row - 1][col - 1] == "1":
                    dp[row][col] = min(dp[row - 1][col - 1], dp[row][col - 1], dp[row - 1][col]) + 1
                    print(dp[row][col])
                    max_area = max(max_area, dp[row][col])
        
        return max_area ** 2