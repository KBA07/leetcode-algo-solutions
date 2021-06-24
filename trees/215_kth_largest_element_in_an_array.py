"""
Medium

6008

374

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
Accepted
935,761
Submissions
1,565,343
"""

"""
Runtime: 64 ms, faster than 73.49% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.1 MB, less than 73.93% of Python3 online submissions for Kth Largest Element in an Array.
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        return heapq.nlargest(k, nums)[-1]

"""
Time limit exceeded
"""
class Solution:
    def findKthLargest(self, nums, k):
        self.data = ["#"]
        self.count = 0
        
        for num in nums:
            self.insert(num)
        
        for _ in range(k):
            val = self.delete()
            
        return val
    
    def insert(self, val):
        self.data.append(val)
        self.count += 1
        self.heapify(sequential=False)
    
    def delete(self):
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        val = self.data.pop()
        self.count -= 1
        self.heapify()
        return val
    
    def isLeaf(self, pos):
        return 2 * pos > self.count
    
    def heapify(self, sequential=True):
        pos = self.count
        
        while pos > 0:
            if not self.isLeaf(pos):
                left = 2 * pos
                right = 2 * pos + 1

                index = left
                if right <= self.count and self.data[right] > self.data[left]:
                    index = right

                if self.data[pos] < self.data[index]:
                    self.data[pos], self.data[index] = self.data[index], self.data[pos]

            if sequential:
                pos -= 1  
            else:
                pos = pos // 2    

"""
Runtime: 3228 ms, faster than 5.02% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.1 MB, less than 42.91% of Python3 online submissions for Kth Largest Element in an Array.
"""
class Solution:
    def findKthLargest(self, nums, k):
        self.data = ["#"]
        self.count = 0
        
        for num in nums:
            self.insert(num)
        
        for _ in range(k):
            val = self.delete()
            
        return val
    
    def insert(self, val):
        self.data.append(val)
        self.count += 1
        
        self.heapifybottom(sequential=False)
    
    def delete(self):
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        val = self.data.pop()
        self.count -= 1
        self.heapifyabove(1) # costly call, let's heapify from above
        return val
    
    def isLeaf(self, pos):
        return 2 * pos > self.count
    
    def heapifyabove(self, pos):
        # print(pos, self.count)
        while pos <= self.count:
            if not self.isLeaf(pos):
                left = 2 * pos
                right = 2 * pos + 1
            
                index = left
                if right <= self.count and self.data[right] > self.data[left]:
                    index = right

                if self.data[pos] < self.data[index]:
                        self.data[pos], self.data[index] = self.data[index], self.data[pos]
                        pos = index
                        continue
            pos =  pos + 1
            
            
    def heapifybottom(self, sequential=True):
        pos = self.count
        
        while pos > 0:
            if not self.isLeaf(pos):
                left = 2 * pos
                right = 2 * pos + 1

                index = left
                if right <= self.count and self.data[right] > self.data[left]:
                    index = right

                if self.data[pos] < self.data[index]:
                    self.data[pos], self.data[index] = self.data[index], self.data[pos]

            if sequential:
                pos -= 1  
            else:
                pos = pos // 2    
