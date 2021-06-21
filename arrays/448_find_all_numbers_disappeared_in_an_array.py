"""
Easy

4382

304

Add to List

Share
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Accepted
390,967
Submissions
691,503
"""

"""
Runtime: 368 ms, faster than 47.74% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.9 MB, less than 82.72% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in nums:
            index = abs(i) - 1
            nums[index] = abs(nums[index]) * - 1
            
        result = []
        
        for index in range(len(nums)):
            if nums[index] > 0:
                result.append(index + 1)
        
        return result
        