"""
79. Word Search
Medium

6210

252

Add to List

Share
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

Accepted
699,722
Submissions
1,846,257
"""

"""
Runtime: 7560 ms, faster than 6.44% of Python3 online submissions for Word Search.
Memory Usage: 14.4 MB, less than 12.48% of Python3 online submissions for Word Search.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        
        for row_index in range(len(board)):
            for col_index in range(len(board[0])):
                if board[row_index][col_index] == word[0] and self.dfs(row_index, col_index, 0):
                    return True
        
        return False
        
    def dfs(self, row_index, col_index, char_count):
        
        if char_count == len(self.word):
            return True
        
        if row_index < 0 or col_index < 0 or row_index >= len(self.board) or col_index >= len(self.board[0]) or self.board[row_index][col_index] != self.word[char_count]:
            return False
        
        temp = self.board[row_index][col_index]
        self.board[row_index][col_index] = ''
        
        found = (self.dfs(row_index + 1, col_index, char_count + 1) or 
            self.dfs(row_index - 1, col_index, char_count + 1) or 
            self.dfs(row_index, col_index + 1, char_count + 1) or 
            self.dfs(row_index, col_index - 1, char_count + 1))
        
        self.board[row_index][col_index] = temp
        return found
