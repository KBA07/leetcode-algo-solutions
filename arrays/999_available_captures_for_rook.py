"""
Easy
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.

 

Example 1:


Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.
Example 2:


Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: The bishops are blocking the rook from attacking any of the pawns.
Example 3:


Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: The rook is attacking the pawns at positions b5, d6, and f5.
 

Constraints:

board.length == 8
board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
Accepted
39,514
Submissions
58,283
"""

"""
Runtime: 32 ms, faster than 70.52% of Python3 online submissions for Available Captures for Rook.
Memory Usage: 14.4 MB, less than 34.64% of Python3 online submissions for Available Captures for Rook.
"""

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:  
        lenChessBoard = len(board)
        rookRow = rookCol = 0
        for rowIndex in range(lenChessBoard):
            for colIndex in range(lenChessBoard):
                if board[rowIndex][colIndex] == 'R':
                    rookRow = rowIndex
                    rookCol = colIndex
                    break
            
            if rookRow and rookCol:
                break
                
        count = 0
        for index in range(rookRow - 1, -1, -1):
            if board[index][rookCol] == 'p':
                count += 1
                break
            elif board[index][rookCol] == 'B':
                break
        
        for index in range(rookRow + 1, lenChessBoard):
            if board[index][rookCol] == 'p':
                count += 1
                break
            elif board[index][rookCol] == 'B':
                break
        
        for index in range(rookCol - 1, -1, -1):
            if board[rookRow][index] == 'p':
                count += 1
                break
            elif board[rookRow][index] == 'B':
                break
        
        for index in range(rookCol + 1, lenChessBoard):
            if board[rookRow][index] == 'p':
                count += 1
                break
            if board[rookRow][index] == 'B':
                break
                
        return count
                
# Solution memory usage can be further optimized by creating a generic function for moving up, down, left or right.