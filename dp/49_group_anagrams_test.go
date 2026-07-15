package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestGroupAnagrams(t *testing.T) {
	assert.Equal(t, groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}),

		[][]string{[]string{"bat"}, []string{"nat", "tan"}, []string{"ate", "eat", "tea"}})
}
