package main

import (
	"slices"
)

func sortedString(s string) string {
	runes := []rune(s)

	slices.Sort(runes)

	return string(runes)
}

/*
Runtime: 12ms Beats 34.13% of users with GoLang
Memory Usage: 10.71 MB Beats 24.94% of users with GoLang
*/
func groupAnagrams(strs []string) [][]string {

	uniqueAnagrams := map[string][]string{}

	for _, str := range strs {
		sortedAnagram := sortedString(str)
		uniqueAnagrams[sortedAnagram] = append(uniqueAnagrams[sortedAnagram], str)
	}

	result := [][]string{}

	for _, value := range uniqueAnagrams {
		result = append(result, value)
	}

	return result
}
