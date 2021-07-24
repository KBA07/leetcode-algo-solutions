"""
1219. Path with Maximum Gold
Medium

1271

41

Add to List

Share
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
Accepted
61,710
Submissions
93,393
"""

"""
Runtime: 1176 ms, faster than 80.23% of Python3 online submissions for Path with Maximum Gold.
Memory Usage: 14.5 MB, less than 18.71% of Python3 online submissions for Path with Maximum Gold.
"""

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return grid
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            curr_gold = grid[row][col]
            grid[row][col] = 0
            
            down = dfs(row + 1, col)
            up = dfs(row - 1, col)
            right = dfs(row, col + 1)
            left = dfs(row, col - 1)
            
            grid[row][col] = curr_gold
             
            return max(up, down, left, right) + curr_gold
        
        
        max_gold = grid[0][0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    max_gold = max(dfs(row, col), max_gold)
        
        return max_gold
