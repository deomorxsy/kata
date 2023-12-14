#include <stdio.h>
// date: 2020-03-03

int main() {
	double pi = 3.14159;
	double raio;
	double area;
	// define the variables with its types.

	scanf("%lf", &raio); // reads the input as double (long float) and assigns the value to the variable
	area = pi * (raio * raio); // calculates the area

	printf("A=%.4lf\n", area); // prints the area, type double (long float), with 4 decimal points.

	return 0;
}

/*
to round: "%2.f";

*/