#include <stdio.h>

int main() {
	int a, b, c, maior;

	scanf("%d %d %d", &a, &b, &c);

	if (a < b || a < c){ // escopo onde a é menor que b OU c.
		if (b > c) { // sendo assim, na 1a situação do escopo, se b for maior que c, então o maior é b.
			maior = b;
		}if (c > b) { // já na 2a situação do escopo, se c for maior que b, então c é o maior.
			maior = c;
			}
	}else{ //o else cobre o escopo da 3a situação, onde a não é menor que nenhum dos dois. Portanto, a seria o maior.
		maior = a;
	}

	printf("%d eh o maior\n", maior);

	return 0;
}