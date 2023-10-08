"""
229. Majority Element II
Medium
9K
387
Companies
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?

Accepted
573.8K
Submissions
1.1M
Acceptance Rate
50.2%
"""

"""
Runtime: 71ms Beats 98.65% of users with Python
Memory Usage: 14.28MB Beats 84.99% of users with Python
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        
        me1, count1, me2, count2 = nums[0], 0, 1, 0
        for num in nums:
            if me1 == num:
                count1 += 1
            elif me2 == num:
                count2 += 1
            elif count1 == 0:
                me1, count1 = num, 1
            elif count2 == 0:
                me2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [num for num in(me1, me2) if nums.count(num) > len(nums) // 3]
