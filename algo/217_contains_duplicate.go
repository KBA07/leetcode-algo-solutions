package main

/*
Runtime: 33ms Beats 22.49% of users with GoLang
Memory Usage: 11.94 MB Beats 43.98% of users with GoLang
*/
func containsDuplicate(nums []int) bool {
	numsMap := map[int]bool{}

	for _, num := range nums {
		if _, ok := numsMap[num]; ok {
			return true
		}

		numsMap[num] = true
	}

	return false
}
