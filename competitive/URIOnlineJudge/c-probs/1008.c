#include <stdio.h>
//date: 2020-03-24
int main() {
	int num, hours; // employee's number; worked hours/month
	float aph, salary; // amount received per hour; salary

	scanf("\n%d \n%d \n%f", &num, &hours, &aph);

	salary = (hours * aph);
	printf("NUMBER = %d\nSALARY = U$ %.2f\n", num, salary);

	return 0;
}