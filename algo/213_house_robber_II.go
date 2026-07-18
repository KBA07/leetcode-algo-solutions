package main

import (
	"fmt"
)

func helper(nums []int, start, end int) int {
	size := end - start
	dp := make([]int, size)

	dp[0] = nums[start]
	dp[1] = max(nums[start], nums[start+1])

	for i := 2; i < size; i++ {
		dp[i] = max(nums[i]+dp[i-2], dp[i-1])
	}

	return dp[size-1]
}

func robCircular(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	if len(nums) == 2 {
		return max(nums[0], nums[1])
	}

	val1 := helper(nums, 0, len(nums)-1)
	val2 := helper(nums, 1, len(nums))

	fmt.Println(val1, val2)
	return max(val1, val2)
}
