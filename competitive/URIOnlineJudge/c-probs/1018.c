#include <stdio.h>
//date: 2020-04-13

int main() {
	// 0 < N < 1000000
	//int cem, cinq, vinte, dez, cinco, dois, um;
	int i, n;
	int cedulas[7] = {100, 50, 20, 10, 5, 2, 1};
	//int acumuladora[7]; // it isn't needed since you just have to return the print.

	scanf("\n%d", &n);
	printf("%d\n", n);

	for (i=0; i < 7; i++) {
		printf("%d nota(s) de R$ %d,00\n", n / cedulas[i], cedulas[i]); //5
		//this could be used: acumuladora[i] = n / cedulas[i];
		n = n % cedulas[i];
	}

	/* another loop with the approach of the accumulator array:

	for (i=0; i < 7; i++)
		printf("%d\n", acumuladora[i]);
	*/
	return 0;
}