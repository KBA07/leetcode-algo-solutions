"""
1526. Minimum Number of Increments on Subarrays to Form a Target Array
Hard

484

33

Add to List

Share
Given an array of positive integers target and an array initial of same size with all zeros.

Return the minimum number of operations to form a target array from initial if you are allowed to do the following operation:

Choose any subarray from initial and increment each value by one.
The answer is guaranteed to fit within the range of a 32-bit signed integer.
 

Example 1:

Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
Example 2:

Input: target = [3,1,1,2]
Output: 4
Explanation: (initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target).
Example 3:

Input: target = [3,1,5,4,2]
Output: 7
Explanation: (initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] 
                                  -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target).
Example 4:

Input: target = [1,1,1,1]
Output: 1
 

Constraints:

1 <= target.length <= 10^5
1 <= target[i] <= 10^5
Accepted
14,087
Submissions
21,656
"""

"""
Runtime: 772 ms, faster than 83.37% of Python3 online submissions for Minimum Number of Increments on Subarrays to Form a Target Array.
Memory Usage: 26.4 MB, less than 70.55% of Python3 online submissions for Minimum Number of Increments on Subarrays to Form a Target Array.
"""

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        totalOpt = target[0]
        Opt = target[0]
        
        for index in range(len(target)):
            if target[index] <= Opt:
                Opt = target[index]
            else:
                totalOpt += target[index] - Opt
                Opt = target[index]
        
        return totalOpt

"""
Runtime: 848 ms, faster than 33.37% of Python3 online submissions for Minimum Number of Increments on Subarrays to Form a Target Array.
Memory Usage: 25.5 MB, less than 91.45% of Python3 online submissions for Minimum Number of Increments on Subarrays to Form a Target Array.
"""
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        dp = [0] * len(target)
        
        dp[0] = target[0]
        
        for index in range(1, len(target)):
            if target[index] <= target[index - 1]:
                dp[index] = dp[index - 1]
            else:
                dp[index] = dp[index-1] + target[index] - target[index - 1]
        
        return dp[-1]
        