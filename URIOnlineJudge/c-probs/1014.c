#include <stdio.h>
//date: 2020-03-28
//program that shows the average consumption of a car.

int main() {
	int km = 0;
	float fuelsp = 0.0; // total amount of fuel spent in the travel
	float average = 0.0;

	scanf("%d %f", &km, &fuelsp);
	average = km / fuelsp;

	printf("%.3f km/l\n", average);
}