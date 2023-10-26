"""
1207. Unique Number of Occurrences
Easy
4.3K
101
company
Apple
company
Amazon
company
Google
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
Accepted
363.6K
Submissions
489.3K
Acceptance Rate
74.3%
"""

"""
Runtime: 0ms Beats 100.00%of users with Go
Memory Usage: 3.25MB Beats 14.39%of users with Go
"""

func uniqueOccurrences(arr []int) bool {
    freq := [2000]int{}
    
    for _, num := range arr {
        freq[num+1000] += 1
    }
    freqSlice := freq[:]
    sort.Slice(freqSlice, func(i int, j int) bool{return freq[i] < freq[j]})
    for i, num := range freqSlice {
        if num != 0 && i < len(freq) - 1 && num == freq[i+1]{
            return false

        }
    }
    return true
}
