"""
338. Counting Bits
Easy
10.5K
475
Companies
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
Accepted
949.5K
Submissions
1.2M
Acceptance Rate
77.5%
"""

"""
Runtime: 149ms Beats 12.82% of users with Python3
Memory Usage: 23.14MB Beats 19.76% of users with Python3
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        def int2bin(n):
            count = 0
            while n:
                remainder = n % 2
                n = n // 2
                count += remainder == 1
            return count

        result = []

        for num in range(n+1):
            result.append(int2bin(num))
        
        return result

"""
Runtime: 86ms Beats 32.96% of users with Python3
Memory Usage: 28.10MB Beats 19.76% of users with Python3
"""

class Solution:
    cache = {}
    def countBits(self, n: int) -> List[int]:

        def int2bin(n):
            if n == 0:
                return 0
    
            if n in self.cache:
                return self.cache[n]

            count = (n % 2) == 1
            count += int2bin(n//2)
            self.cache[n] = count
            return count

        result = []

        for num in range(n+1):
            result.append(int2bin(num))
        
        return result
        