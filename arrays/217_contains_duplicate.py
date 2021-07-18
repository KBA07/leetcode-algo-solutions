"""
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
773,947
Submissions
1,361,769
"""

"""
Runtime: 136 ms, faster than 10.50% of Python3 online submissions for Contains Duplicate.
Memory Usage: 21.5 MB, less than 21.13% of Python3 online submissions for Contains Duplicate.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        
        for number in nums:
            try:
                nums_dict[number] += 1
                return True
            except KeyError:
                nums_dict[number] = 1
        return False

"""
Runtime: 120 ms, faster than 64.80% of Python3 online submissions for Contains Duplicate.
Memory Usage: 20.1 MB, less than 59.72% of Python3 online submissions for Contains Duplicate.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True
        
        return False
    