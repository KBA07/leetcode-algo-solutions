"""
32. Longest Valid Parentheses
Hard
11.7K
362
Companies
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
Accepted
652.9K
Submissions
2M
Acceptance Rate
33.2%
"""

"""
Runtime: 37ms Beats 97.78% of users with Python3
Memory Usage: 17.21MB Beats 12.57% of users with Python3
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        char_stack = [] 
        index_stack = [-1]
        max_len = 0

        for index, char in enumerate(s):
            if char == '(':
                char_stack.append(char)
                index_stack.append(index)
            else:
                if char_stack and char_stack[-1] == '(':
                    char_stack.pop()
                    index_stack.pop()
                    max_len = max(max_len, index - index_stack[-1])
                else:
                    index_stack.append(index)
        return max_len
