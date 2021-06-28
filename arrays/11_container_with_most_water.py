"""
Medium

9988

734

Add to List

Share
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
Accepted
982,213
Submissions
1,851,520
"""

"""
Runtime: 684 ms, faster than 88.06% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.5 MB, less than 48.55% of Python3 online submissions for Container With Most Water.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        max_area = 0
        
        while(start < end):
            
            if height[end] > height[start]:
                max_area = max(max_area, height[start] * (end - start))
                start += 1
            else:
                max_area = max(max_area, height[end] * (end - start))
                end -= 1
        return max_area
