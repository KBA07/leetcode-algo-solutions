"""
733. Flood Fill
Easy

2238

264

Add to List

Share
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n
Accepted
248,743
Submissions
442,415
"""

"""
Runtime: 68 ms, faster than 94.70% of Python3 online submissions for Flood Fill.
Memory Usage: 14.3 MB, less than 90.75% of Python3 online submissions for Flood Fill.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        def dfs(image, sr, sc, color, newColor):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] == newColor or image[sr][sc] != color :
                return
            
            # prevColor = image[sr][sc]
            image[sr][sc] = newColor
            
            dfs(image, sr + 1, sc, color, newColor)
            dfs(image, sr - 1, sc, color, newColor)
            dfs(image, sr, sc + 1, color, newColor)
            dfs(image, sr, sc - 1, color, newColor)
        
        dfs(image, sr, sc, image[sr][sc], newColor)
        
        return image
        