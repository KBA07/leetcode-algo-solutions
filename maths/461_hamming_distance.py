"""
461. Hamming Distance
Easy

2327

179

Add to List

Share
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
 

Constraints:

0 <= x, y <= 231 - 1
Accepted
407,362
Submissions
554,472
"""

"""
Runtime: 32 ms, faster than 61.39% of Python3 online submissions for Hamming Distance.
Memory Usage: 14.2 MB, less than 44.07% of Python3 online submissions for Hamming Distance.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x or y:
            result += (x % 2) ^ (y % 2)
            
            x = x >> 1
            y = y >> 1
            
        return result

