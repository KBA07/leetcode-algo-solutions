package main

/*
Runtime: 0ms Beats 100% of users with GoLang
Memory Usage: 4.42 MB Beats 15.76% of users with GoLang
*/
func isValid(s string) bool {
	characters := []rune(s)

	stack := []rune{}

	for _, char := range characters {

		switch char {

		case ')':
			if len(stack) != 0 && stack[len(stack)-1] == '(' {
				stack = stack[:len(stack)-1]
				continue
			}

		case '}':
			if len(stack) != 0 && stack[len(stack)-1] == '{' {
				stack = stack[:len(stack)-1]
				continue
			}

		case ']':
			if len(stack) != 0 && stack[len(stack)-1] == '[' {
				stack = stack[:len(stack)-1]
				continue
			}
		}

		stack = append(stack, char)

	}

	return len(stack) == 0

}
