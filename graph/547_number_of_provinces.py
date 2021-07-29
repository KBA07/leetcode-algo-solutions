"""
547. Number of Provinces
Medium

3462

196

Add to List

Share
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
Accepted
300,095
Submissions
486,848
"""

"""
Runtime: 176 ms, faster than 97.19% of Python3 online submissions for Number of Provinces.
Memory Usage: 15.1 MB, less than 26.05% of Python3 online submissions for Number of Provinces.
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0] * len(isConnected)
        
        def visit(source):
            for dest in range(len(isConnected)):
                if isConnected[source][dest] == 1 and not visited[dest]:
                    visited[dest] = 1
                    visit(dest)
        
        province = 0
        for city in range(len(visited)):
            
            if not visited[city]:
                visit(city)
                province += 1
        
        return province

"""
Runtime: 296 ms, faster than 17.71% of Python3 online submissions for Number of Provinces.
Memory Usage: 14.5 MB, less than 89.17% of Python3 online submissions for Number of Provinces.
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = [0] * len(isConnected)
        bucket_list = []
        province = 0
        for city in range(len(visited)):
            
            if not visited[city]:
                bucket_list.append(city)
                
                while bucket_list:
                    current_city = bucket_list.pop(0)
                    visited[current_city] = 1
                    
                    for dest in range(len(isConnected)):
                        if isConnected[current_city][dest] and not visited[dest]:
                            bucket_list.append(dest)
                
                province += 1
        return province