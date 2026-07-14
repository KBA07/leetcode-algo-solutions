package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestMaxProfit(t *testing.T) {
	assert.Equal(t, maxProfit([]int{7, 1, 5, 3, 6, 4}), 7)
	assert.Equal(t, maxProfit([]int{1}), 0)
}
