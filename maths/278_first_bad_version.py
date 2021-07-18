"""
278. First Bad Version
Easy

2451

894

Add to List

Share
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
Accepted
599,746
Submissions
1,555,216
"""

"""
Runtime: 32 ms, faster than 54.33% of Python3 online submissions for First Bad Version.
Memory Usage: 14.2 MB, less than 43.56% of Python3 online submissions for First Bad Version.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # start = 1
        # end = n
        
        def helper(start, end):
            if start == end:
                return start
            
            
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                return helper(start, mid)
            
            return helper(mid + 1, end)
        
        return helper(1, n)
                