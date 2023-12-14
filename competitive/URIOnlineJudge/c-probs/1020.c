#include <stdio.h>
//date:2020-04-14
int main() {
	int agedays = 0;
	int acc[3]; // accumulator
	int tempo[3] = {365, 30, 1}; //{year/month}
	int i;
	scanf("\n%d", &agedays);

	for (i=0; i < 3; i++)
	{
		acc[i] = agedays / tempo[i]; // 1
		agedays = agedays % tempo[i];
	}


	printf( "%d ano(s)\n%d mes(es)\n%d dia(s)\n", acc[0], acc[1], acc[2]);
}