#!/usr/bin/R

somador = 0.0
sum_array <- function(a) {
	for (item in a) {
		somador = somador + item
	}
	print(somador)
}

sum_array(c(1, 5.2, 4, 0, -1))