package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsValid(t *testing.T) {

	// assert.Equal(t, isValid("()"), true)
	assert.Equal(t, isValid("){"), true)
	// assert.Equal(t, isValid("()[]{}"), true)
	// assert.Equal(t, isValid("(]"), false)
}
