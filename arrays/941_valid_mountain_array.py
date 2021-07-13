"""
941. Valid Mountain Array
Easy

1085

102

Add to List

Share
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
Accepted
177,777
Submissions
544,729
"""

"""
Runtime: 349 ms, faster than 5.02% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15.6 MB, less than 58.55% of Python3 online submissions for Valid Mountain Array.
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        arr_len = len(arr)
        
        # go up
        while i < arr_len - 1 and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == arr_len - 1:
            return False
        
        while i < arr_len - 1 and arr[i] > arr[i+1]:
            i += 1
        
        return i == arr_len - 1