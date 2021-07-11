"""
881. Boats to Save People
Medium

1403

51

Add to List

Share
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 

Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
Accepted
77,240
Submissions
156,576
"""

"""
Runtime: 460 ms, faster than 41.67% of Python3 online submissions for Boats to Save People.
Memory Usage: 21.1 MB, less than 52.45% of Python3 online submissions for Boats to Save People.
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        start = 0
        end = len(people) - 1
        count = 0
        while start < end:
            if people[start] + people[end] <= limit:
                start += 1
                
            end -= 1
            count += 1
        
        if start == end:
            count += 1
        return count