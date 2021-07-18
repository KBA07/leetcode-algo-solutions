"""
349. Intersection of Two Arrays
Easy

1636

1632

Add to List

Share
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
Accepted
512,256
Submissions
771,683
"""

"""
Runtime: 40 ms, faster than 93.39% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.3 MB, less than 73.56% of Python3 online submissions for Intersection of Two Arrays.
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set()
        
        for num in nums1:
            nums1_set.add(num)
        
        result = set()
        for num in nums2:
            if num in nums1_set:
                result.add(num)
                
        return list(result)


"""
Runtime: 48 ms, faster than 57.59% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.5 MB, less than 13.15% of Python3 online submissions for Intersection of Two Arrays.
"""
# Assuming that if the array is sorted, solve this on time - O(N) and space - O(1)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        i = 0
        j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            num1 = nums1[i]
            num2 = nums2[j]
            
            if num1 == num2:
                result.append(num1)
                while i < len(nums1) and num1 == nums1[i]:
                    i += 1
                while j < len(nums2) and num2 == nums2[j]:
                    j += 1
                continue
            
            if num1 < num2:
                i += 1
            else:
                j += 1
        
        return result