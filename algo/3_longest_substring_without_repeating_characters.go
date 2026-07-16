package main

/*
Runtime: 10ms Beats 24.34% of users with GoLang
Memory Usage: 5.28 MB Beats 24.50% of users with GoLang
*/
func lengthOfLongestSubstring(s string) int {
	charSet := map[string]bool{}
	start := 0
	end := 0
	maxLength := 0

	for end < len(s) {

		if _, ok := charSet[string(s[end])]; ok {
			delete(charSet, string(s[start]))
			start += 1
		} else {
			charSet[string(s[end])] = true
			end += 1

		}

		if end-start > maxLength {
			maxLength = end - start
		}

	}

	return maxLength
}
