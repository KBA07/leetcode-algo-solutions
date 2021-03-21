"""
Easy
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
"""
"""
Runtime: 168 ms, faster than 63.08% of Python3 online submissions for Majority Element.
Memory Usage: 15.6 MB, less than 10.45% of Python3 online submissions for Majority Element.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        int_dict = {}
        for element in nums:
            try:
                int_dict[element] += 1
            except KeyError:
                int_dict[element] = 1
        
        max_element = nums[0]
        max_element_value = int_dict[max_element]
        
        for key, value in int_dict.items():
            if value > max_element_value:
                max_element = key
                max_element_value = value
                
        return max_element

"""
Runtime: 160 ms, faster than 87.55% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 52.09% of Python3 online submissions for Majority Element.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = None
        count = 0
        
        for num in nums:
            
            if count == 0:
                me = num
                
            if num != me:
                count -= 1
            else:
                count += 1
        
        return me
