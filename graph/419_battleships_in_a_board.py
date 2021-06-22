"""
419. Battleships in a Board
Medium

1002

629

Add to List

Share
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.
 

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?

Accepted
118,219
Submissions
164,971
"""
"""
Runtime: 92 ms, faster than 16.69% of Python3 online submissions for Battleships in a Board.
Memory Usage: 14.9 MB, less than 29.59% of Python3 online submissions for Battleships in a Board.
"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        battelship_count = 0
        for row_index in range(len(board)):
            for col_index in range(len(board[0])):
                battelship_count += self.findbattleship(board, row_index, col_index)
        
        return battelship_count
    
    def findbattleship(self, board, row_index, col_index):
        if row_index < 0 or row_index >= len(board) or col_index < 0 or col_index >= len(board[0]) or board[row_index][col_index] == '.':
            return 0
        
        board[row_index][col_index] = '.' # sink the current
        
        self.findbattleship(board, row_index + 1, col_index)
        self.findbattleship(board, row_index - 1, col_index)
        self.findbattleship(board, row_index, col_index + 1)
        self.findbattleship(board, row_index, col_index - 1)
        
        return 1
