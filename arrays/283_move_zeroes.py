"""
Easy
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
Accepted
1,076,459
Submissions
1,836,379
"""
"""
Runtime: 48 ms, faster than 80.61% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.3 MB, less than 88.74% of Python3 online submissions for Move Zeroes.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fp = 0
        ip = 0
        while(ip < len(nums)):
            
            if nums[ip] != 0:
                nums[ip], nums[fp] = nums[fp], nums[ip]
                fp += 1
                
            ip += 1
        return nums