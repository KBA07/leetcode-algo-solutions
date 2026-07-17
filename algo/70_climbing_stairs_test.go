package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestClimbStairs(t *testing.T) {

	assert.Equal(t, climbStairs(3), 3)
	assert.Equal(t, climbStairs(2), 2)
	assert.Equal(t, climbStairs(45), 1836311903)

}
