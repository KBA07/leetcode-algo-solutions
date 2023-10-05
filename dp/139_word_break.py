"""
139. Word Break
Medium
16.3K
708
Companies
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Accepted
1.5M
Submissions
3.2M
Acceptance Rate
46.2%
"""

"""
Time Limit Exceeded
"""

# Back Track
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        cache = {}

        def backtrack(pos: int) -> bool:
            nonlocal cache

            if pos == len(s): return True
            if pos in cache: return cache[pos]

            for i in range(pos, len(s)):
                subStr = s[pos:i+1]
                # print(subStr, pos, i - pos)
                if subStr in wordDict and backtrack(i+1):
                    cache[pos] = True
                    print(cache)
                    return cache[pos]
            
            return False
        
        return backtrack(0)


"""
Runtime: 43ms Beats 65.23% of users with Python3
Memory Usage: 16.26MB Beats 93.50% of users with Python3
"""

# Tabulation DP 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * len(s)

        for i in range(len(s)):
            if s[:i+1] not in wordDict:
                for j in range(i):
                    if dp[j] and s[j+1:i+1] in wordDict:
                        dp[i] = True
                        break
            else:
                dp[i] = True

        return dp[-1]
                 


