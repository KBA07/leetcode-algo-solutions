"""
Easy
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
Example 4:

Input: columnTitle = "FXSHRXW"
Output: 2147483647
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
Accepted
367,730
Submissions
644,913
"""
"""
Runtime: 36 ms, faster than 48.39% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 14.2 MB, less than 47.41% of Python3 online submissions for Excel Sheet Column Number.
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        relativeNumber = 64
        power = 1
        val = 0
        
        for index in range(len(columnTitle)-1,-1,-1):
            val += power * (ord(columnTitle[index]) - 64)
            power = power * 26
            
        return val
