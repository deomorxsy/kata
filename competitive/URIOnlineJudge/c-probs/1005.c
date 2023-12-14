#include <stdio.h>
//date: 2020-03-23

int main() {
	double a, b, MEDIA;
	double pa = 3.5;
	double pb = 7.5;

	scanf("\n%lf \n%lf", &a, &b); // Associa os endereços de memória ao valor de input

	MEDIA = ((pa * a) + (pb * b))/(pa + pb); 
	printf("MEDIA = %.5lf\n", MEDIA);
}