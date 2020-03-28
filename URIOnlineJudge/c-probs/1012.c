#include <stdio.h>

int main() {
	double a, b, c;
	double trirec, circle, trapez, square, rect;
	double pi = 3.14159;

	scanf("%lf %lf %lf", &a, &b, &c);

	trirec = (a * c)/2.0; // área do triângulo retângulo
	circle = pi * (c * c); // área do círculo
	trapez = (1.0/2.0) * (a + b) * c; // área do trapézio
	square = (b * b); // área do quadrado
	rect = (a * b); // área do retângulo

	printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\nQUADRADO: %.3lf\nRETANGULO: %.3lf\n", trirec, circle, trapez, square, rect);

	return 0;
}