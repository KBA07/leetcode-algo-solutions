package main

import (
	"fmt"
	"slices"
)

func binarySearch(nums []int, start, end, target int) int {
	// add boundry checks
	for start < end {
		mid := (start + end) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			start = mid + 1
		} else {
			end = mid
		}
	}

	return -1
}

// we can't sort because the index will change
func twoSum(nums []int, target int) []int {

	slices.Sort(nums)
	fmt.Println(nums)

	for index, value := range nums {
		search := target - value

		if searchIndex := binarySearch(nums, index, len(nums), search); searchIndex > 0 {
			return []int{index, searchIndex}
		}
	}

	return []int{-1, -1}
}

func twoSumUsingMap(nums []int, target int) []int {
	numMap := map[int][]int{}

	for index, num := range nums {
		numMap[num] = append(numMap[num], index)
	}

	for num, indexes := range numMap {

		required := target - num

		if required == num && len(indexes) > 1 {
			return indexes[:2]
		} else {
			if _, ok := numMap[required]; ok {
				return []int{numMap[required][0], indexes[0]}
			}
		}

	}

	return []int{-1, -1}
}

/*
Runtime: 1ms Beats 51.84% of users with GoLang
Memory Usage: 5.77 MB Beats 68.47% of users with GoLang
*/
func twoSumUsingMapFinal(nums []int, target int) []int {
	numsMap := map[int]int{}

	for index, num := range nums {
		difference := target - num

		if _, ok := numsMap[difference]; ok {
			return []int{index, numsMap[difference]}
		}

		numsMap[num] = index
	}

	return []int{-1, -1}
}
