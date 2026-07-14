package main

import (
	"fmt"
)

/*
Runtime: 0ms Beats 100% of users with GoLang
Memory Usage: 6.44 Beats 36.48% of users with GoLang
*/

func maxProfit(prices []int) int {
	if len(prices) == 1 {
		return 0
	}

	profit := 0
	for i := 0; i < len(prices)-1; i++ {
		if prices[i] < prices[i+1] {
			profit += prices[i+1] - prices[i]
		}
	}

	return profit
}

func main() {
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
	fmt.Println(maxProfit([]int{1, 2, 3, 4, 5}))
	fmt.Println(maxProfit([]int{7, 6, 4, 3, 1}))
}
