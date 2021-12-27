"""
1282. Group the People Given the Group Size They Belong To
Medium

845

438

Add to List

Share
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

 

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
 

Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
Accepted
71,654
Submissions
84,271
"""

"""
Runtime: 76 ms, faster than 70.68% of Python3 online submissions for Group the People Given the Group Size They Belong To.
Memory Usage: 14.5 MB, less than 43.37% of Python3 online submissions for Group the People Given the Group Size They Belong To.
"""

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = {}
        
        for person, group_size in enumerate(groupSizes):
            try:
                group_map[group_size].append(person)
            except KeyError:
                group_map[group_size] = [person]
        
        result = []
        for size, group in group_map.items():
            for index in range(0, len(group) + 1, size):
                
                chunk = group[index:index + size]
                if chunk:
                    result.append(chunk)
                
        return result
    