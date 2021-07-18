"""
1. Two Sum
Easy

22622

762

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
Accepted
4,568,784
Submissions
9,667,741
"""

"""
Runtime: 56 ms, faster than 89.42% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 40.99% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        result = []
        for index in range(len(nums)):
            difference = target - nums[index]
            
            if difference in nums_map:
                result.append(index)
                result.append(nums_map[difference])
                return result
            
            nums_map[nums[index]] = index
