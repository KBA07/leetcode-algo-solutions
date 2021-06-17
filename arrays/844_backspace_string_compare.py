"""
844. Backspace String Compare
Easy

2601

119

Add to List

Share
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?

Accepted
302,564
Submissions
640,979
"""

"""
Success
Details 
Runtime: 36 ms, faster than 23.07% of Python3 online submissions for Backspace String Compare.
Memory Usage: 14.4 MB, less than 17.49% of Python3 online submissions for Backspace String Compare.
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s = list(s)
        backspace_count = 0
        for index in range(len(s)-1, -1, -1):
            
            if s[index] == '#':
                backspace_count += 1
                del s[index]
                continue
            
            if backspace_count:
                del s[index]
                backspace_count -= 1
        
        print(s)
        
        t = list(t)
        backspace_count = 0
        for index in range(len(t)-1, -1, -1):
            
            if t[index] == '#':
                backspace_count += 1
                del t[index]
                continue
            
            if backspace_count:
                del t[index]
                backspace_count -= 1
        print(t)
        
        return s == t

"""
Runtime: 28 ms, faster than 86.09% of Python3 online submissions for Backspace String Compare.
Memory Usage: 14.2 MB, less than 51.34% of Python3 online submissions for Backspace String Compare.
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_point = len(s) - 1
        s_backspace = 0
        t_point = len(t) - 1
        t_backspace = 0
        
        
        while t_point >= 0 or s_point >= 0:
            
            while s_point >= 0:
                
                if s[s_point] == '#':
                    s_backspace += 1
                    s_point -= 1
                    continue
                
                if s_backspace:
                    s_point -= 1
                    s_backspace -= 1
                    continue
                
                break
            
            while t_point >= 0:
                
                if t[t_point] == '#':
                    t_backspace += 1
                    t_point -= 1
                    continue
                
                if t_backspace:
                    t_point -= 1
                    t_backspace -= 1
                    continue
                
                break
            
            if (s_point >= 0 and t_point < 0) or (s_point < 0 and t_point >= 0):
                return False
            
            if s[s_point] != t[t_point]:
                return False
            
            s_point -= 1
            t_point -= 1
        
        return True