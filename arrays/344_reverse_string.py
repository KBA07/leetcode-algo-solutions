"""
344. Reverse String
Easy

2669

805

Add to List

Share
Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
 

Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Accepted
1,107,380
Submissions
1,549,015
"""

"""
Runtime: 208 ms, faster than 36.10% of Python3 online submissions for Reverse String.
Memory Usage: 47.2 MB, less than 5.54% of Python3 online submissions for Reverse String.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(str_list, start, end):
            if start < end:
                str_list[start], str_list[end] = str_list[end], str_list[start]
                helper(str_list, start + 1, end - 1)
        
        helper(s, 0, len(s) - 1)
        return s
        