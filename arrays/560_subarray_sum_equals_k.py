"""
560. Subarray Sum Equals K
Medium

8284

279

Add to List

Share
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
Accepted
524,420
Submissions
1,200,766
"""

"""
Time Limit Exceeded
61 / 89 test cases passed.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = collections.defaultdict(int)
        
        for i in range(len(nums)):
            sum_map[nums[i]] += 1
            for j in range(i+1, len(nums)):
                sum_map[sum(nums[i:j+1])] += 1
        
        return sum_map[k]

"""
Time Limit Exceeded
72 / 89 test cases passed.
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = [0] * (len(nums) + 1)
        
        for index in range(1, len(nums) + 1):
            sum_map[index] = sum_map[index - 1] + nums[index - 1]

        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                if sum_map[j] - sum_map[i] == k:
                    count += 1
        
        return count