"""
136. Single Number
Easy

6728

218

Add to List

Share
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
Accepted
1,226,587
Submissions
1,824,769
"""

"""
Runtime: 132 ms, faster than 71.70% of Python3 online submissions for Single Number.
Memory Usage: 16.8 MB, less than 19.48% of Python3 online submissions for Single Number.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()
        
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                num_set -= {num}
                
        for element in num_set:
            pass
        
        return element
