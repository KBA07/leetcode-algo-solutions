"""
Medium

541

66

Add to List

Share
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

 

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
Example 3:

Input: nums = [6,6,0,1,1,4,6]
Output: 2
Example 4:

Input: nums = [1,5,6,14,15]
Output: 1
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
Accepted
25,883
Submissions
45,993
"""

"""
Runtime: 316 ms, faster than 98.72% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
Memory Usage: 24.2 MB, less than 25.32% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
"""

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5: # len = 4 and below, in that case we can sink all to get 0
            return 0
        
        start = [float('inf')] * 4
        end = [float('-inf')] * 4
        
        for num in nums:
            if num < start[-1]:
                start[-1] = num
                start.sort()
            
            if num > end[0]:
                end[0] = num
                end.sort()
        
        result = float('inf')
        for index in range(len(start)):
            result = min(result, end[len(end) - 4 + index] - start[index])   
        
        return result

"""
Runtime: 376 ms, faster than 32.84% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
Memory Usage: 24.2 MB, less than 43.05% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5: # len = 4 and below, in that case we can sink all to get 0
            return 0
        
        result = float('inf')
        for index in range(4):
            result = min(result, heapq.nlargest(4, nums)[3 - index] - heapq.nsmallest(4, nums)[index])   
        
        return result