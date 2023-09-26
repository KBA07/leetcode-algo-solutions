"""
316. Remove Duplicate Letters
Medium
7.5K
484
Companies
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Accepted
253K
Submissions
545.9K
Acceptance Rate
46.3%
"""

"""
Runtime: 36ms Beats 89.29% of users with Python3
Memory Usage: 16.30MB Beats 82.57% of users with Python3
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        frequency = defaultdict(int)
        seen = set()
        stack = []

        for char in s:
            frequency[char] += 1
        
        for char in s:
            if char in seen:
                frequency[char] -= 1
                continue
            
            while stack and stack[-1] > char and frequency[stack[-1]] > 0:
                lt = stack.pop()
                seen.remove(lt)
            
            stack.append(char)
            frequency[char] -= 1
            seen.add(char)

        return ''.join(stack)
                