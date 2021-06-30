"""
Medium

3705

114

Add to List

Share
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
Accepted
290,438
Submissions
435,508
"""

"""
Runtime: 152 ms, faster than 57.69% of Python3 online submissions for Max Area of Island.
Memory Usage: 16.2 MB, less than 67.71% of Python3 online submissions for Max Area of Island.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                island_area = self.get_area(grid, row_index, col_index)
                
                if island_area > max_area:
                    max_area = island_area
        
        return max_area
    
    def get_area(self, grid, row_index, col_index):
        if row_index < 0 or col_index < 0 or row_index > len(grid) - 1 or col_index > len(grid[0]) - 1 or grid[row_index][col_index] == 0:
            return 0
        
        grid[row_index][col_index] = 0
        
        return 1 + self.get_area(grid, row_index - 1, col_index) + self.get_area(grid, row_index + 1, col_index) + self.get_area(grid, row_index, col_index - 1) + self.get_area(grid, row_index, col_index + 1)
