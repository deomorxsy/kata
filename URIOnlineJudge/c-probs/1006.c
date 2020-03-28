#include <stdio.h>

int main() {
	double a, b, c, MEDIA;
	double pa = 2;
	double pb = 3;
	double pc = 5;

	scanf("\n%lf \n%lf \n%lf", &a, &b, &c);

	MEDIA = ((pa * a) + (pb * b) + (pc * c))/(pa + pb + pc); 
	/* notice that without the parentheses in the summation of the numerator,
	the last element of the sum would be divided first. Precedence matters in C.*/
	printf("MEDIA = %.1lf\n", MEDIA);
}
