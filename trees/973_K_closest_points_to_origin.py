"""
973. K Closest Points to Origin
Medium

3299

166

Add to List

Share
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104
Accepted
496,198
Submissions
762,971
"""

"""
32/84 test cases passed
heap implementation is wrong
"""
class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.data = ['#']
        self.count = 0
        
        distance_points = {}
        
        for point in points:
            distance = self.get_distance(point[0], point[1])
            
            self.insert(distance)
            try:
                distance_points[distance].append(point)
            except KeyError:
                distance_points[distance] = [point]
        
        res = []
        for _ in range(k):
            res.extend(distance_points.pop(self.remove(), []))
             
        return res
    
    @staticmethod
    def get_distance(x, y):
        return ((y)**2 + (x)**2) ** 0.5 
        
    
    def insert(self, distance):
        self.data.append(distance)
        self.count += 1
        
        n = self.count
        
        while n > 1:
            parent = n // 2
            
            if self.data[n] > self.data[parent]:
                break
                
            self.data[parent], self.data[n] = self.data[n], self.data[parent] 
            n = parent
      
    def remove(self):
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        val = self.data.pop()
        self.count -= 1
        n = 1
        while n <= self.count:
            if not self.isleaf(n):
                left_child = 2 * n
                right_child = 2 * n + 1
                
                index = left_child
                if right_child <= self.count and self.data[right_child] < self.data[left_child]:
                    index = right_child
                
                if self.data[n] < self.data[index]:
                    break 
                
                self.data[index], self.data[n] = self.data[n], self.data[index]
                n = index
            n += 1
        return val
                    
    def isleaf(self, pos):
        return 2 * pos > self.count

"""
Runtime: 768 ms, faster than 26.19% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 20.4 MB, less than 22.56% of Python3 online submissions for K Closest Points to Origin.
"""

import heapq

class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.data = []
        self.count = 0
        
        distance_points = {}
        
        for point in points:
            distance = self.get_distance(point[0], point[1])
            self.data.append(distance)
            try:
                distance_points[distance].append(point)
            except KeyError:
                distance_points[distance] = [point]
            
        res = heapq.nsmallest(k, self.data)
        final_rest = []
        for index in range(len(res)):
            final_rest.extend(distance_points.pop(res[index], []))
        
        return final_rest
    
    @staticmethod
    def get_distance(x, y):
        return ((y)**2 + (x)**2) ** 0.5 