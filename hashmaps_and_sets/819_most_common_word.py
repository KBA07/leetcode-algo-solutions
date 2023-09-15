"""
819. Most Common Word
Easy
1.6K
3K
Companies
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
 

Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
Accepted
333.3K
Submissions
749K
Acceptance Rate
44.5%
"""

"""
Runtime: 54ms Beats 12.26% of users with Python3
Memory Usage: 16.50MB Beats 23.45% of users with Python3
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        def getWord(paragraph):
            last_word = ''
            index = 0
            while index < len(paragraph):
                if paragraph[index].isalpha():
                    last_word += paragraph[index].lower()
                    index += 1
                    continue

                while index < len(paragraph) and not paragraph[index].isalpha():
                    index += 1

                yield last_word
                last_word = ''
            
            if last_word: yield last_word
                
                
        paragraph.strip()
        word_map = defaultdict(int)
        for word in getWord(paragraph):
            print(word)
            word_map[word] += 1

        for word in banned:
            word_map.pop(word, None)
        
        target_word = None
        rep = 0

        print(word_map)
        for word in word_map:
            if word_map[word] > rep:
                rep = word_map[word]
                target_word = word
        
        return target_word
        