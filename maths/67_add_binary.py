"""
67. Add Binary
Easy
8.5K
838
Companies
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
Accepted
1.2M
Submissions
2.3M
Acceptance Rate
52.6%
"""

"""
Runtime: 44ms, Beats 76.83% of users with Python3
Memory Usage: 16.35mb, Beats 47.18% of users with Python3
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def checkAndGetBinary(array: list, index: int) -> int:
            if -1 < index < len(array):
                return int(array[index])
            
            return 0

        
        a_index = len(a) - 1
        b_index = len(b) - 1
        carry_prev = 0
        result = ''

        while a_index > -1 or b_index > -1:
            temp_sum = checkAndGetBinary(a, a_index) + checkAndGetBinary(b, b_index) + carry_prev
            carry_prev = temp_sum // 2
            result = str(temp_sum % 2) + result

            a_index -= 1
            b_index -= 1
        
        if carry_prev:
            result = str(carry_prev) + result

        return result

"""
Runtime: 36ms, Beats 95.53% of users with Python3
Memory Usage: 16.43mb, Beats 14.51% of users with Python3
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def checkAndGetBinary(array: list, index: int) -> int:
            if -1 < index:
                return int(array[index])
            return 0

        
        a_index = len(a) - 1
        b_index = len(b) - 1
        carry_prev = 0
        result = []

        while a_index > -1 or b_index > -1:
            temp_sum = checkAndGetBinary(a, a_index) + checkAndGetBinary(b, b_index) + carry_prev
            carry_prev = temp_sum // 2
            result.append(temp_sum % 2)

            a_index -= 1
            b_index -= 1
        
        if carry_prev:
            result.append(carry_prev)

        result.reverse()
        return ''.join(str(binary) for binary in result)
