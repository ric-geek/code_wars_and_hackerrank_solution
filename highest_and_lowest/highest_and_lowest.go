package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func main() {

	var mny string = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"

	s := strings.Split(mny, " ")

	intSlice := make([]int, len(s))

	for i, c := range s {

		intSlice[i], _ = strconv.Atoi(c)

	}

	sort.Ints(intSlice)

	ric := strconv.Itoa(intSlice[0]) + " " + strconv.Itoa(intSlice[1])

	fmt.Println(ric)
	fmt.Println(s)
	fmt.Println(intSlice)

}
