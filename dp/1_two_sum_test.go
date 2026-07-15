package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// func TestTwoSum(t *testing.T) {
// 	assert.Equal(t, twoSum([]int{2, 7, 11, 15}, 9), []int{0, 1})
// 	assert.Equal(t, twoSum([]int{3, 2, 4}, 6), []int{1, 2})
// 	assert.Equal(t, twoSum([]int{3, 3}, 6), []int{0, 1})
// 	// assert.Equal(t, twoSum([]int{1, 1}, 1), []int{-1, -1})
// }

func TestTwoSumUsingMap(t *testing.T) {
	assert.Equal(t, twoSumUsingMap([]int{2, 7, 11, 15}, 9), []int{1, 0})
	assert.Equal(t, twoSumUsingMap([]int{3, 2, 4}, 6), []int{2, 1})
	assert.Equal(t, twoSumUsingMap([]int{3, 3}, 6), []int{0, 1})
	// assert.Equal(t, twoSum([]int{1, 1}, 1), []int{-1, -1})
}
