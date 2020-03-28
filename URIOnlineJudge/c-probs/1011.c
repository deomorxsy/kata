#include <stdio.h>

int main(int argc, char *argv[])
{
	double radius;
	double pi = 3.14159;
	double vol;

	scanf("%lf", &radius);

	vol = (4.0/3.0) * pi * (radius * radius * radius);
	printf("VOLUME = %.3lf\n", vol);

	return 0;
}