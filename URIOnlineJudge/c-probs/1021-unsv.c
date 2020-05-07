#include <stdio.h>
#include <math.h>

int main() {
	int notas[6] = {100, 50, 20, 10, 5, 2};
	float moedas[6] = {1.00, 0.50, 0.25, 0.10, 0.05, 0.01};
	// it has to be float
	int accnot[6], accmoe[6]; // n de ocorrencias

	int index;
	float valor = 0.00;

	scanf("\n%f", &valor); 
	//the \n is important. Don't forget the & to get the variable adress.

	printf("NOTAS:\n");
	for (index=0; index < 6; index++)
	{
		accnot[index] = (int) (valor / notas[index]);
		valor = fmod(valor, (float) notas[index]);//fmod
		printf("%d nota(s) de R$ %d.00\n", accnot[index], notas[index]);

	}

	//printf("VALOR = %f.\n", valor);

	printf("MOEDAS:\n");
	for (index=0; index < 6; index++)
	{
		accmoe[index] = (int) (valor / moedas[index]);// (int)
		valor = fmod(valor, moedas[index]);//fmod
		//printf("VALOR = %f.\n", valor);
		index > 4 ? printf("%d moeda(s) de R$ %.2f\n", accmoe[index] * 0.001, moedas[index]): printf("%d moeda(s) de R$ %.2f\n", accmoe[index], moedas[index]);
		//printf("%d moeda(s) de R$ %.2f\n", accmoe[index], moedas[index]);
	}

}
