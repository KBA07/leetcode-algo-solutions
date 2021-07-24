"""
739. Daily Temperatures
Medium

4745

137

Add to List

Share
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
Accepted
266,812
Submissions
407,518
"""

"""
Time Limit Exceeded
30 / 47 test cases passed.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        
        for i in range(len(temperatures)):
            # current_temp = temperatures[i]
            difference = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    difference = (j - i)
                    break
            result.append(difference)
        
        return result

"""
Runtime: 1196 ms, faster than 79.11% of Python3 online submissions for Daily Temperatures.
Memory Usage: 25.5 MB, less than 26.17% of Python3 online submissions for Daily Temperatures.
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temp:
                curr = stack.pop()
                answer[curr] = i - curr
            
            stack.append(i)
        
        return answer

