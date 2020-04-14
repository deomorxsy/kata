#include <stdio.h>
//date:2020-04-13
int main() {
	int dusec = 0; //duration in seconds of a certain event in a factory
	int i, acc[3];
	int hour = 3600; //1h has 60min. 1min has 60sec. 60x60=3600.

	scanf("\n%d", &dusec);

	//printf("%d", dusec / 60);

	for (i=0; i < 3; i++)
	{
		acc[i] = dusec / hour; //hour = 3600
		//printf("acc[%d] vale: %d\n", i, acc[i]); // 0
		//9
		dusec = dusec % hour;
		//printf("resto: %d\n", dusec); // 556

		hour = hour / 60;
		//printf("%d:", acc[i]);
		i < 2 ? printf("%d:", acc[i]): printf("%d\n", acc[i]);
		//printf("horas: %d\n", hour); // 60
		/*if (i = 2) {NOTE: buffer overflow?
			acc[i] = dusec;
			printf("acc[%d] vale: %d\n", i, acc[i]);
		}*/
	}

	//printf("%d", acc[2]);

	return 0;
}