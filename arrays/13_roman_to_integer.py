"""
13. Roman to Integer
Easy
11.7K
673
Companies
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
Accepted
2.9M
Submissions
4.9M
Acceptance Rate
59.0%
"""

"""
Runtime: 48ms, Beats 94.15% of users with Python3
Memory Usage: 16.12mb, Beats 98.02%of users with Python3
"""

class Solution:
    ROMAN_TO_INT = {
        "I": 1, 
        "V": 5, 
        "X": 10, 
        "L": 50, 
        "C": 100, 
        "D": 500, 
        "M": 1000
    }
    EXCEPTION = {
        "I": {"V": 4, "X": 9},
        "X": {"L": 40, "C": 90},
        "C": {"D": 400, "M": 900}
    }

    def romanToInt(self, s: str) -> int:

        index = 0
        value = 0

        while index < len(s):
            if s[index] in self.EXCEPTION.keys() and index + 1 < len(s) and self.EXCEPTION[s[index]].get(s[index + 1]):
                value += self.EXCEPTION[s[index]].get(s[index + 1])
                index += 2
                continue
            
            value += self.ROMAN_TO_INT[s[index]]
            index += 1
    
        return value
    
"""
Runtime: 59ms,Beats 69.92%of users with Python3
Memory Usage: 16.35mb, Beats 51.91%of users with Python3
"""

class Solution:
    ROMAN_TO_INT = {
        "I": 1, 
        "V": 5, 
        "X": 10, 
        "L": 50, 
        "C": 100, 
        "D": 500, 
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:

        index = 0
        value = 0

        while index < len(s):

            if index < (len(s) - 1) and self.ROMAN_TO_INT[s[index]] < self.ROMAN_TO_INT[s[index + 1]]:
                value -= self.ROMAN_TO_INT[s[index]]
            else:
                value += self.ROMAN_TO_INT[s[index]]
            
            index += 1

        return value
