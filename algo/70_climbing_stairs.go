package main

var cache = map[int]int{}

/*
Runtime: 0ms Beats 100% of users with GoLang
Memory Usage: 3.92 MB Beats 22.01% of users with GoLang
*/
func climbStairs(n int) int {
	if read, ok := cache[n]; ok {
		return read
	}

	if n == 1 {
		return 1

	}

	if n == 2 {
		return 2
	}

	val := climbStairs(n-1) + climbStairs(n-2)
	cache[n] = val

	return val
}
