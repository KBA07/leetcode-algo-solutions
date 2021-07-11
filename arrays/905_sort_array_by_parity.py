"""
905. Sort Array By Parity
Easy

1890

99

Add to List

Share
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
Accepted
348,148
Submissions
464,070
"""

"""
Runtime: 88 ms, faster than 25.79% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 15.1 MB, less than 57.20% of Python3 online submissions for Sort Array By Parity.
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            if nums[start] % 2 == 0:
                start += 1
                continue
            
            if nums[end] % 2 != 0:
                end -= 1
                continue

            nums[start], nums[end] = nums[end], nums[start]
        
        return nums
