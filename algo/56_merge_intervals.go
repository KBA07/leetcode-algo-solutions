package main

import (
	"fmt"
	"sort"
)

func sortSlice(intervals [][]int) {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
}

/*
Runtime: 1ms Beats 73.01% of users with GoLang
Memory Usage: 8.80 MB Beats 7.68% of users with GoLang
*/
func merge(intervals [][]int) [][]int {
	sortSlice(intervals)

	// fmt.Println(intervals)
	res := make([][]int, 0, len(intervals))
	res = append(res, intervals[0]) // take the first interval

	// [[1,3],[2,6],[8,10],[15,18]]
	// res = [1,3]
	// 1st Iteration [1,3] and [2,6]

	for i := 1; i < len(intervals); i++ {

		if res[len(res) - 1][1] < intervals[i][0] // the start time is greater than end time
		{
			// append
			res = append(res, intervals[i])
		} else {
			// extend the last value of interval

			res[len(res) - 1][0] = min(res[len(res) - 1][0], intervals[i][0])
			res[len(res) - 1][1] = max(res[len(res) - 1][1], intervals[i][1])
		}
	}

	return res
}
