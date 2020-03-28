#include <stdio.h>
//date: 2020-03-24

int main() {
	char name;
	double fixsal, sales, total; // fixed salary, sale's total and total amount.

	scanf("%s %lf %lf", &name, &fixsal, &sales);

	total = (0.15 * sales) + fixsal; // the total is 15% of all sales added to the fixed salary.
	printf("TOTAL = R$ %.2lf\n", total);

}