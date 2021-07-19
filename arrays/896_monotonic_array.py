"""
896. Monotonic Array
Easy

1101

47

Add to List

Share
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].  An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Return true if and only if the given array nums is monotonic.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
Example 4:

Input: nums = [1,2,4,5]
Output: true
Example 5:

Input: nums = [1,1,1]
Output: true
 

Note:

1 <= nums.length <= 50000
-100000 <= nums[i] <= 100000
Accepted
160,811
Submissions
277,985
"""

"""
Runtime: 492 ms, faster than 42.18% of Python3 online submissions for Monotonic Array.
Memory Usage: 20.5 MB, less than 85.36% of Python3 online submissions for Monotonic Array.
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        
        for index in range(len(nums) - 1):
            if nums[index] < nums[index + 1]:
                decreasing = False
            
            if nums[index] > nums[index + 1]:
                increasing = False
        
        return increasing or decreasing
            
        