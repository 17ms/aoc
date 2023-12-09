package main

import (
	"encoding/json"
	"fmt"
	"os"
	"sort"
	"strings"
)

func collect(left, right string) ([]interface{}, []interface{}) {
	var leftSlice []interface{}
	var rightSlice []interface{}

	json.Unmarshal([]byte(left), &leftSlice)
	json.Unmarshal([]byte(right), &rightSlice)

	return leftSlice, rightSlice
}

func cmp(left, right any) int {
	lv, llok := left.([]interface{})
	rv, rlok := right.([]interface{})

	switch {
	case !llok && !rlok: // both ints
		return int(left.(float64) - right.(float64))
	case !llok: // left int
		lv = []any{left}
	case !rlok: // right int
		rv = []any{right}
	}

	// copied from: https://github.com/mnml/aoc/blob/main/2022/13/1.go#L53
	for i := 0; i < len(lv) && i < len(rv); i++ {
		if c := cmp(lv[i], rv[i]); c != 0 {
			return c
		}
	}

	return len(lv) - len(rv)
}

func solve() (int, int) {
	input, _ := os.ReadFile("input.txt")
	total := make([]interface{}, 0)
	pairs := strings.Split(strings.TrimSpace(string(input)), "\n\n")

	sum := 0
	decoder := 1

	for i, p := range pairs {
		packets := strings.Split(p, "\n")
		pkg1, pkg2 := collect(packets[0], packets[1])
		if cmp(pkg1, pkg2) <= 0 {
			sum += i + 1
			total = append(total, pkg1, pkg2)
		} else {
			total = append(total, pkg2, pkg1)
		}
	}

	extra1, extra2 := collect("[[2]]", "[[6]]")
	total = append(total, extra1, extra2)

	sort.Slice(total, func(i, j int) bool {
		return cmp(total[i], total[j]) <= 0
	})

	for i, pkg := range total {
		str := fmt.Sprintf("%v", pkg)
		if str == "[[6]]" || str == "[[2]]" {
			decoder *= i + 1
		}
	}

	return sum, decoder
}

func main() {
	resultA, resultB := solve()
	fmt.Printf("A: %d\nB: %d\n", resultA, resultB)
}
