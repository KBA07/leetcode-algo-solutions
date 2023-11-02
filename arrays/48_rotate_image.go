"""
48. Rotate Image
Medium
16.4K
721
company
Google
company
Amazon
company
Cisco
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
Accepted
1.5M
Submissions
2M
Acceptance Rate
72.9%
"""

"""
Runtime: 1ms Beats 82.72% of users with Go
Memory Usage: 2.26MB Beats 53.47% of users with Go
"""

func rotate(matrix [][]int)  {
    n := len(matrix)
    a := matrix

    for i := 0; i < n; i++ {
        for j := i; j < n; j++ {
            a[i][j], a[j][i] = a[j][i], a[i][j]
        }
    }

    for i := 0; i < n; i++ {
        l, r := 0, n-1

        for l < r {
            a[i][l], a[i][r] = a[i][r], a[i][l]
            l++
            r--
        }
    }
}