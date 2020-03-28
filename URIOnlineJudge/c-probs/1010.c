#include <stdio.h>
#include <stdlib.h>

int main() {
	int codo1, namba1, codo2, namba2;
	float price1, price2;

	scanf("%d %d %f", &codo1, &namba1, &price1);
	scanf("%d %d %f", &codo2, &namba2, &price2);

	printf("VALOR A PAGAR: R$ %.2f\n", (namba1 * price1) + (namba2 * price2));

	return 0;
}
