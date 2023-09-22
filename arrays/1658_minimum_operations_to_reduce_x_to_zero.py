"""
1658. Minimum Operations to Reduce X to Zero
Medium
5.2K
108
Companies
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
Accepted
173.2K
Submissions
435K
Acceptance Rate
39.8%
"""

"""
Runtime: 966ms Beats 56.34% of users with Python3
Memory Usage: 38.24MB Beats 13.25% of users with Python3
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)

        if x > total_sum:
            return -1 

        k = total_sum - x
        sum_map = defaultdict(int)
        sum_map[0] = -1
        curr_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            curr_sum += num

            if(curr_sum - k) in sum_map:
                max_len = max(max_len, i - sum_map[curr_sum - k])
            
            sum_map[curr_sum] = i
        
        # print(sum_map, k)
        if not max_len:
            if not k:
                return len(nums)
            else:
                return -1
        else:
            return len(nums) - max_len
        