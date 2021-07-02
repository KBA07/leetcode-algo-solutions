"""
Medium

7486

200

Add to List

Share
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
Accepted
747,207
Submissions
1,710,339
"""

"""
Runtime: 20 ms, faster than 99.34% of Python3 online submissions for House Robber.
Memory Usage: 14.3 MB, less than 18.45% of Python3 online submissions for House Robber.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for index in range(2, len(nums)):
            dp[index] = max(nums[index] + dp[index-2], dp[index - 1])
        
        return dp[index]

# Memory efficient implementation

"""
Runtime: 32 ms, faster than 65.25% of Python3 online submissions for House Robber.
Memory Usage: 14 MB, less than 91.73% of Python3 online submissions for House Robber.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        third = nums[0]
        second = max(nums[0], nums[1])
        
        for index in range(2, len(nums)):
            first = max(nums[index] + third, second)
            third = second
            second = first
        
        return first