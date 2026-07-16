package main

/*
Runtime: 0ms Beats 100% of users with GoLang
Memory Usage: 11.38 MB Beats 19.92% of users with GoLang
*/
func maxProfit(prices []int) int {
	minPrice := prices[0]
	profit := 0

	for _, price := range prices {

		if price < minPrice {
			minPrice = price
		}

		if profit < price-minPrice {
			profit = price - minPrice
		}
	}

	return profit
}
