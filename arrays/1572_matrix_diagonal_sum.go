"""
1572. Matrix Diagonal Sum
Easy
3.3K
45
company
Google
company
Adobe
company
Apple
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
Accepted
304.2K
Submissions
367.9K
Acceptance Rate
82.7%
Seen this question in a real interview before?
1/4
"""

"""
Runtime: 10ms Beats 73.23%of users with Go
Memory Usage: 5.53MB Beats 20.87%of users with Go
"""

func diagonalSum(mat [][]int) int {
    sum := 0

    for i := 0; i < len(mat); i++ {
        for j := 0; j < len(mat[0]); j++ {
            if i == j {
                sum += mat[i][j]
                mat[i][j] = 0
            }
            if len(mat[0]) - 1 - i == j {
                sum += mat[i][j]
                mat[i][j] = 0
            }
        }
    }
    return sum
    
}

func diagonalSum(mat [][]int) int {
    sum := 0
    mid := len(mat) / 2

    for i := 0; i < len(mat); i++ {
        sum += mat[i][i]
        sum += mat[len(mat) - 1 - i][i]
    }
    if len(mat) % 2 == 1 { // odd case will have common diagonal
        sum -= mat[mid][mid]
    }
    return sum
}

