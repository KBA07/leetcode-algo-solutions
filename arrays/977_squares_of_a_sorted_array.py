"""
977. Squares of a Sorted Array
Easy

2766

117

Add to List

Share
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
Accepted
541,870
Submissions
757,898
"""

"""
Runtime: 232 ms, faster than 53.66% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.9 MB, less than 89.18% of Python3 online submissions for Squares of a Sorted Array.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for index, num in enumerate(nums):
            nums[index] = num ** 2
        
        nums.sort()
        return nums
        