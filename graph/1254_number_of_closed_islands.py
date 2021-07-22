"""
1254. Number of Closed Islands
Medium

1031

28

Add to List

Share
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
Accepted
53,661
Submissions
86,137
"""

"""
Runtime: 132 ms, faster than 79.99% of Python3 online submissions for Number of Closed Islands.
Memory Usage: 14.7 MB, less than 81.91% of Python3 online submissions for Number of Closed Islands.
"""

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # self.answer = 0
        
        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            
            if grid[row][col] == 1: # Land seen
                return 1
            
            grid[row][col] = 1 # Man, this was so silly mistake

            up = dfs(grid, row+1, col)
            down = dfs(grid, row-1, col)
            right = dfs(grid, row, col+1)
            left = dfs(grid, row, col-1)
            return up and down and left and right
                    
        answer = 0
        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                if grid[row_index][col_index] == 0: # posibility of an island
                    answer += dfs(grid, row_index, col_index)
        
        return answer
    
"""
Runtime: 124 ms, faster than 94.12% of Python3 online submissions for Number of Closed Islands.
Memory Usage: 14.7 MB, less than 81.91% of Python3 online submissions for Number of Closed Islands.
"""

class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0

            if grid[row][col] == 1:
                return 1

            grid[row][col] = 1

            # now check the conditions for up, down, left, right
            up = dfs(grid, row+1, col)
            down = dfs(grid, row-1, col)
            right = dfs(grid, row, col+1)
            left = dfs(grid, row, col-1)

            return up and down and left and right
    
        answer = 0
        
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                
                if grid[rowIdx][colIdx] == 0:
                    answer += dfs(grid, rowIdx , colIdx)
        return answer


        