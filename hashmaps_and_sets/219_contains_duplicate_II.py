"""
219. Contains Duplicate II
Easy

1433

1446

Add to List

Share
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
Accepted
344,287
Submissions
877,108
"""

"""
Runtime: 592 ms, faster than 5.27% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 28.5 MB, less than 5.41% of Python3 online submissions for Contains Duplicate II.
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        nums_dict = {}
        for index, num in enumerate(nums):
            
            if num in nums_dict:
                if abs(index - nums_dict[num]) <= k:
                    return True
                
            nums_dict[num] = index
        return False
