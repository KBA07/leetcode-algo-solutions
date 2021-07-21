"""
1525. Number of Good Ways to Split a String
Medium

662

19

Add to List

Share
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.

 

Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
Example 2:

Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").
Example 3:

Input: s = "aaaaa"
Output: 4
Explanation: All possible splits are good.
Example 4:

Input: s = "acbadbaada"
Output: 2
 

Constraints:

s contains only lowercase English letters.
1 <= s.length <= 10^5
Accepted
34,009
Submissions
48,907
"""

"""
Runtime: 160 ms, faster than 84.92% of Python3 online submissions for Number of Good Ways to Split a String.
Memory Usage: 14.8 MB, less than 69.48% of Python3 online submissions for Number of Good Ways to Split a String.
"""

class Solution:
    def numSplits(self, s: str) -> int:
        p_map = {}
        q_map = {}
        
        for char in s:
            try:
                q_map[char] += 1
            except KeyError:
                q_map[char] = 1
                
        # print(q_map)
        
        
        gs_count = 0
        for char in s:
            try:
                p_map[char] += 1
            except KeyError:
                p_map[char] = 1
            
            q_map[char] -= 1
            if q_map[char] == 0:
                q_map.pop(char)
            
            # print(p_map, q_map)
            
            if len(q_map) == len(p_map):
                gs_count += 1
        
        return gs_count
        