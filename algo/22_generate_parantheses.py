"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
"""
Runtime: 28 ms, faster than 45.47% of Python online submissions for Generate Parentheses.
Memory Usage: 12.7 MB, less than 96.13% of Python online submissions for Generate Parentheses.
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret_list = []
        pat = ""
        lef = n
        rig = n

        def handler(left, right, pattern):
            if (left > right) or (left < 0) or (right < 0):
                # Right should always be less than or equal to left
                return

            if left == 0 and right == 0:
                ret_list.append(pattern)

            handler(left - 1, right, pattern + '(')
            handler(left, right - 1, pattern + ')')

        handler(lef, rig, pat)
        return ret_list
