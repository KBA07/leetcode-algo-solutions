"""
365. Water and Jug Problem
Medium
1.3K
1.4K
Companies
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
 

Example 1:

Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example 
Example 2:

Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false
Example 3:

Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true
 

Constraints:

1 <= jug1Capacity, jug2Capacity, targetCapacity <= 106
Accepted
87.1K
Submissions
224.8K
Acceptance Rate
38.8%
"""

"""
Runtime: 588ms Beats 40.21% of users with Python3
Memory Usage: 287.26MB Beats 12.73% of users with Python3
"""

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        measured = set()

        def dfs(current):
            
            if current == targetCapacity:
                return True
            
            if current in measured or current < 0 or current > jug1Capacity + jug2Capacity:
                return False
            
            measured.add(current)

            return dfs(current + jug1Capacity) or dfs(current - jug1Capacity) or dfs(current + jug2Capacity) or dfs(current - jug2Capacity)
        

        return dfs(0)

"""
Runtime: 412ms Beats 54.95% of users with Python3
Memory Usage: 37.60MB Beats 61.05% of users with Python3
"""

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # BFS
        measured = set()
        stack = [0]
        choices = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]

        while stack:

            current = stack.pop()

            for choice in choices:
                total = current + choice
                if total == targetCapacity:
                    return True
                
                if total not in measured and (total > 0  and total < jug1Capacity + jug2Capacity):
                    measured.add(total)
                    stack.append(total)
            
        return False