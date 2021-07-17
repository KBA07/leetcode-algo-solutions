"""
1007. Minimum Domino Rotations For Equal Row
Medium

1335

196

Add to List

Share
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length == bottoms.length <= 2 * 104
1 <= tops[i], bottoms[i] <= 6
Accepted
125,228
Submissions
245,718
"""

"""
Runtime: 1076 ms, faster than 87.11% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
Memory Usage: 15.2 MB, less than 63.61% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
"""

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def helper(value, A, B):
            swaps = 0
            
            for index in range(0, len(A)):
                if value == A[index]:
                    continue
                elif value == B[index]:
                    swaps += 1
                    continue
                else:
                    return float('inf')
            return swaps
        
        min_value = min(helper(tops[0], tops, bottoms), helper(bottoms[0], tops, bottoms))
        min_value = min(min_value, helper(tops[0], bottoms, tops))
        min_value = min(min_value, helper(bottoms[0], bottoms, tops))
        
        return -1 if min_value == float('inf') else min_value
