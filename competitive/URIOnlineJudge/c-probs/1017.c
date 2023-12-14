#include <stdio.h>
//date: 2020-04-11

int main() {
	//amount of spent fuel of a car
	// that does 12km/L.
	int spfuel = 12;

	int sptime = 1; //spent time
	int avgspeed = 1; //average speed during the trip km/h
	int total = 1;

	scanf("%d %d", &sptime, &avgspeed);
	total = sptime * avgspeed;

	printf("%.3f\n", ((double) total) / ((double) spfuel));


	return 0;
}