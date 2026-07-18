package main

/*
Runtime: 0ms Beats 100% of users with GoLang
Memory Usage: 3.93 MB Beats 64.94% of users with GoLang
*/
func rob(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	dp := make([]int, len(nums))

	dp[0] = nums[0]
	dp[1] = max(nums[1], nums[0])

	for i := 2; i < len(nums); i++ {
		dp[i] = max(nums[i]+dp[i-2], dp[i-1])
	}

	return dp[len(nums)-1]
}
