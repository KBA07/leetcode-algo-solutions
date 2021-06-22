"""
Share
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 

Constraints:

n == image.length
n == image[i].length
1 <= n <= 20
images[i][j] is either 0 or 1.
Accepted
245,257
Submissions
312,016
"""
"""
Runtime: 52 ms, faster than 57.66% of Python3 online submissions for Flipping an Image.
Memory Usage: 14.3 MB, less than 21.50% of Python3 online submissions for Flipping an Image.
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for row in image:
            
            start = 0
            end = len(row) - 1
            
            while start < end:
                row[start], row[end] = row[end] ^ 1, row[start] ^ 1 # xor with 1, 0 - 1 and 1 - 0
                start += 1
                end -= 1
            
            if len(row) % 2 != 0:
                # odd number, flip the middle bit
                row[start] = row[start] ^ 1
                
        
        return image
