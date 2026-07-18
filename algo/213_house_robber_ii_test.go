package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRobCircular(t *testing.T) {
	// assert.Equal(t, robCircular([]int{1, 2, 1, 1}), 3)

	assert.Equal(t, robCircular([]int{1, 2, 3, 1}), 4)
}
