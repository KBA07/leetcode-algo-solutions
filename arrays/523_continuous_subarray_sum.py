"""
523. Continuous Subarray Sum
Medium
5.1K
496
Companies
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
Accepted
409.7K
Submissions
1.4M
Acceptance Rate
28.5%
"""

"""
Runtime: 951ms Beats 28.45% of users with Python3
Memory Usage: 36.02MB Beats 72.64% of users with Python3
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        if len(nums) < 2:
            return False

        sum_map = defaultdict(int)
        sum_map[0] = -1
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            remainder = curr_sum % k
            
            if remainder in sum_map and i - sum_map[remainder] > 1:
                return True
            
            if remainder not in sum_map:
                sum_map[remainder] = i
        
        return False
