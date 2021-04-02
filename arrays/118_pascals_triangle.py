"""
Easy
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
Accepted
475,617
Submissions
859,164
"""

"""
Runtime: 32 ms, faster than 58.48% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14.3 MB, less than 58.53% of Python3 online submissions for Pascal's Triangle.
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for rows in range(numRows):
            rows_list = []
            for cols in range(rows+1):
                if cols == 0 or cols == rows:
                    rows_list.append(1)
                else:
                    rows_list.append(pascal[rows-1][cols] + pascal[rows-1][cols-1])
            pascal.append(rows_list)
        return pascal
    