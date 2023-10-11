"""
276. Paint Fence
Medium
1.5K
377
company
Google
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.

 

Example 1:


Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.
Example 2:

Input: n = 1, k = 1
Output: 1
Example 3:

Input: n = 7, k = 2
Output: 42
 

Constraints:

1 <= n <= 50
1 <= k <= 105
The testcases are generated such that the answer is in the range [0, 231 - 1] for the given n and k.
Accepted
102.4K
Submissions
226.5K
Acceptance Rate
45.2%
"""

"""
Runtime: 1ms Beats 88.24%of users with Go
Memory Usage: 1.98MB Beats 58.82%of users with Go
"""
func numWays(n int, k int) int {
    if n < 2 {
        return k
    }

    dp := make([]int, n+1)

    dp[1] = k
    dp[2] = k * k

    for i := 3; i < n+1; i++ {
        dp[i] = (dp[i-1] + dp[i-2]) * (k-1)
    }
    fmt.Println(dp)
    return dp[n]
}

"""
Runtime: 0ms Beats 100.00%of users with Go
Memory Usage: 1.88MB Beats 100.00%of users with Go
"""

func numWays(n int, k int) int {
    if n < 2 {
        return k
    }

    twoPostBack := k
    onePostBack := k * k

    for i := 3; i < n+1; i++ {
        curr := (k-1) * (onePostBack + twoPostBack)
        twoPostBack = onePostBack
        onePostBack = curr
    }
    return onePostBack
}

