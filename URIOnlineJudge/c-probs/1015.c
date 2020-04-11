#include <stdio.h>
#include <math.h>

/*
URI 1015.c
*/

double mypow(double base, int exp) {
	// a function that calculates the power of a number
	int i; // the increment used in for.
	double pot = 1.0; 
	// stores the neutral element of multiplication, 1, in order to
	// increment the multiplications with the assignment operator "*=".
	for (i=1; i <= exp; i++)
		pot *= base; 

	return pot;
}

int main() {
	double x1, y1, x2, y2;
	double sumcord, distance;

	scanf("%lf %lf %lf %lf", &x1, &y1, &x2, &y2);

	sumcord = mypow((x2 - (x1)), 2) + mypow((y2 - (y1)), 2);
	//printf("sumcord é igual a %.4lf.\n", sumcord);
	distance = sqrt(sumcord);

	printf("%.4lf\n", distance);

	return 0;
}
