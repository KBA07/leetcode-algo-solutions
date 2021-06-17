"""
200. Number of Islands
Medium

8812

249

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
Accepted
1,086,028
Submissions
2,158,618
"""


"""
Runtime: 144 ms, faster than 34.62% of Python online submissions for Number of Islands.
Memory Usage: 21.4 MB, less than 41.55% of Python online submissions for Number of Islands.
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def find_island(grid, index_row, index_col):
            if (0 > index_row) or (index_row > len(grid) - 1) or (0 > index_col) or (index_col > len(grid[0]) - 1) or grid[index_row][index_col] == '0':
                return 0
            
            grid[index_row][index_col] = '0'
            
            find_island(grid, index_row - 1, index_col)
            find_island(grid, index_row + 1, index_col)
            find_island(grid, index_row, index_col - 1)
            find_island(grid, index_row, index_col + 1)
            
            return 1
        
        island_count = 0
        
        for index_row in range(len(grid)):
            for index_col in range(len(grid[0])):
                island_count += find_island(grid, index_row, index_col)
                
        return island_count
                                          