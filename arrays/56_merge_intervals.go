"""
56. Merge Intervals
Medium
21K
708
company
Facebook
company
Amazon
company
Google
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
Accepted
2.1M
Submissions
4.4M
Acceptance Rate
46.6%
"""

"""
Runtime: 42ms Beats 5.00% of users with Go
Memory Usage: 57.50% of users with Go
"""

func min(a,b int)int {
    if a < b {
        return a
    }
    return b
}

func max(a,b int)int {
    if a > b {
        return a
    }
    return b
}

func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func(i, j int) bool {return intervals[i][0] < intervals[j][0]})
    results := [][]int{}
    currentInterval := []int{intervals[0][0], intervals[0][1]}

    for _, interval := range intervals {
        fmt.Println(currentInterval, interval)
        if currentInterval[1] >= interval[0] {
            currentInterval[0] = min(currentInterval[0], interval[0])
            currentInterval[1] = max(currentInterval[1], interval[1])
        } else {
            results = append(results, []int{currentInterval[0], currentInterval[1]})
            currentInterval[0], currentInterval[1] = interval[0], interval[1]
        }
    }
    results = append(results, currentInterval)
    return results
}