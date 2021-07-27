"""
1277. Count Square Submatrices with All Ones
Medium

2311

38

Add to List

Share
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
Accepted
114,822
Submissions
156,429
"""

"""
Runtime: 600 ms, faster than 86.44% of Python3 online submissions for Count Square Submatrices with All Ones.
Memory Usage: 16.3 MB, less than 86.73% of Python3 online submissions for Count Square Submatrices with All Ones.
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    # this means that we need to increment the result
                    if i == 0 or j == 0: # Means we have hit the first row or colomn:
                        result += 1
                    else:
                        # Get the min of the surronding 3 elements
                        val = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + matrix[i][j]
                        result += val
                        matrix[i][j] = val
        
        return result