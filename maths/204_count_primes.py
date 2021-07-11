"""
204. Count Primes
Easy

3462

835

Add to List

Share
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
Accepted
509,426
Submissions
1,552,919
"""

"""
Runtime: 3204 ms, faster than 22.79% of Python3 online submissions for Count Primes.
Memory Usage: 52.7 MB, less than 96.80% of Python3 online submissions for Count Primes.
"""

class Solution:
    prime_set = set()
    def countPrimes(self, n: int) -> int:
        
        primes = [True] * n
        count = 0
        
        i = 2
        while i ** 2 < n:
            if primes[i]:
                j = 2
                while j * i < n:
                    primes[j * i] = False
                    j += 1
            i += 1
        
        for index in range(2, n):
            if primes[index]:
                count += 1
        return count
        