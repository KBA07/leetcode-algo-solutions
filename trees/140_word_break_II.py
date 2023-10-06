"""
140. Word Break II
Hard
6.5K
518
Companies
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
Accepted
537.5K
Submissions
1.2M
Acceptance Rate
46.4%
"""

"""
Runtime: 42ms Beats 27.40% of users with Python3
Memory Usage: 16.33MB Beats 41.37% of users with Python3
"""

class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word: str) -> None:
        curr = self.root
        for let in word:
            if let not in curr:
                curr[let] = {}
            curr = curr[let]
        
        curr['*'] = ''
    def search(self, word: str) -> bool:
        curr = self.root
        for let in word:
            if let not in curr: return False
            curr = curr[let]
        return '*' in curr

class Solution:
    def backtrack(self, remStr: str, curr_result: str) -> None:
        print(remStr)
        if not remStr:
            self.results.append(curr_result)
            return

        word = ''
        for i, let in enumerate(remStr):
            word += let
            print(word)
            if self.trie.search(word):
                self.backtrack(remStr[i+1:], curr_result + f" {word}")

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.trie = Trie()
        self.results = []
        for word in wordDict:
            self.trie.insert(word)
        
        word = ''
        for i, let in enumerate(s):
            word += let
            print(word)
            if self.trie.search(word):
                print("search")
                print(s.split(word)[1])
                self.backtrack(s[i+1:], word)

        return self.results