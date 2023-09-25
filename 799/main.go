package main

var verbose bool = false

type Pair struct {
	row   int
	index int
}

func NewPair(row int, index int) Pair {
	return Pair{row, index}
}

func recusion_champagneTower(poured int, query_row int, query_glass int, cache map[Pair]float64) float64 {
	if verbose {
		println(poured, query_row, query_glass)
	}
	pair := NewPair(query_row, query_glass)
	val, ok := cache[pair]
	if ok {
		return val
	}
	if poured == 0 {
		return 0.
	} else if query_row == 0 {
		return float64(poured)
	}
	res := 0.
	if query_glass > 0 {
		res += max(recusion_champagneTower(poured, query_row-1, query_glass-1, cache)-1, 0.) / 2
	}
	if query_glass < query_row {
		res += max(recusion_champagneTower(poured, query_row-1, query_glass, cache)-1, 0.) / 2
	}
	cache[pair] = res
	return res
}

func champagneTower(poured int, query_row int, query_glass int) float64 {
	cache := make(map[Pair]float64)
	res := recusion_champagneTower(poured, query_row, query_glass, cache)
	return min(res, 1.)
}

func isEqual(a, b float64) bool {
	if a < b {
		return isEqual(b, a)
	}
	return (a - b) <= 1e-5
}

func main() {
	input := []int{1, 1, 1, 2, 1, 1, 100000009, 33, 17, 25, 6, 1}
	output := []float64{0.00000, 0.50000, 1.00000, 0.18750}
	idx := -1
	for i := 0; i < len(input); i += 3 {
		idx += 1
		res := champagneTower(input[i], input[i+1], input[i+2])
		println("test", idx, "is", res, output[idx], isEqual(res, output[idx]))
	}
}
