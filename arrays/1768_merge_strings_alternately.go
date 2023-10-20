"""
1768. Merge Strings Alternately
Easy
3.1K
55
company
Amazon
company
Apple
company
Google
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
Accepted
447.3K
Submissions
565.1K
Acceptance Rate
79.2%
"""

"""
Runtime: 1ms Beats 74.41%of users with Go
Memory Usage: 2.11MB Beats 60.33%of users with Go
"""

func mergeAlternately(word1 string, word2 string) string {
    result := []byte{}

    point1, point2 := 0, 0

    for point1 < len(word1) && point2 < len(word2) {
        result = append(result, word1[point1])
        result = append(result, word2[point2])

        point1++
        point2++
    }

    if point1 < len(word1) {
        result = append(result, word1[point1:]...)
    }

    if point2 < len(word2) {
        result = append(result, word2[point2:]...)
    }

    return string(result)
}
