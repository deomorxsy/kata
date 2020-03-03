#include <stdio.h>
// date: 2020-03-03

int main() {
	float pi = 3.14159;
	float raio;
	float area;
	// define the variables with its types.

	scanf("%f", &raio); // reads the input as float and assigns the value to the variable
	area = pi * (raio * 2); // calculates the area

	printf("A=%4f", area); // prints the area, type float, with 4 decimal points.

}