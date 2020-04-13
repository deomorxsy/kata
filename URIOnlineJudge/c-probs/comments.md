```c
#include <stdio.h>
// date: 2020-03-03

int main() {
	// double pi = 3.14159;
	double raio;
	double area;
	// define the variables with its types.

	scanf("%lf", &raio); // reads the input as double (long float) and assigns the value to the variable
	area = 3.14159 * raio * raio; // calculates the area

	printf("A=%.4lf\n", area); // prints the area, type double (long float), with 4 decimal points.

	return 0;
}

/*
to round: "%2.f";

*/
```

#### 2020-03-20

Pro scanf, a quebra de linha vem antes do código de formatação da função. Ex: ```scanf("\n%d \n%d", &a, &b);```

Nos casos em que você esquece de se referir à variável com o **Operador de Endereços**, ou *Adress Operator* (*&*), o sistema(arch linux, shell) retorna o seguinte:
```Falha de segmentação (imagem do núcleo gravada)```
#

Leitura adicional:

+ ["Why do we use address operator '&' in the C language?"](https://www.quora.com/Why-do-we-use-address-operator-in-the-C-language)
+ [Endereços e Ponteiros](https://www.ime.usp.br/~pf/algoritmos/aulas/pont.html)


#### 2020-03-23

- **scanf**: não se separa códigos de formatação com vírgula.
	- *errado*: ```scanf("\n%lf, \n%lf", a, b);```
	- *correto*: ```scanf("\n%lf \n%lf", a, b);```

URI 1008
```c
#include <stdio.h>

int main() {
	int num, hours; // employee's number; worked hours/month
	float aph, salary; // amount received per hour; salary

	scanf("\n%d \n%d \n%f", &num, &hours, &aph);

	salary = hours * aph;
	printf("NUMBER = %d \nSALARY = U$ %.2f\n", num, salary);

	/*the C pre-processor translates the "\n" above as escape sequence.
	The first is useful to separate the input from the ouput in the CLI.
	The second, to separate the second sign, "SALARY", from the first.
	So it isn't printed in the same line. 
	The last one separates the OUTPUT from the PROMPT of the CLI.  */
}
```


#### 2020-03-27

Aritmética com endereços. Enquanto no *python* podemos incrementar o index de um array com o seguinte ```lista[i+1]```, no C, somamos o incremento diretamente à variável (é claro que aparentemente com pointers): ```lista+1```

Assim, [...]"Em regra geral, se **M** é o nome de uma matriz e **i** é uma variável do tipo **int**, então **M + i** é equivalente a **SM[i]**. [...]".

Portanto, ```lista+1 = lista[i+1]```.

Trecho do *Livro Treinamento em Linguagem C*, da Victorine:

Utilizando esse conceito, podemos extrair uma substring de uma string somando ao seu endereço um número inteiro que indique o byte onde começará nossa substring. Veja o exemplo:

```c
/* str5.c */
/* Mostra o uso da aritmética com endereços */
#include <stdio.h>
#include <stdlib.h>

int main()
{
	char salute[] = "Saudações, ";
	char nome[80];
	printf("Digite o seu nome: ");
	gets(nome);
	printf("%s%s\n", salute, nome + 5);
	system("PAUSE");
	return 0;
}
```

#### Pointing to something: Retrieving an Adress
> [Reading](https://www.cprogramming.com/tutorial/c/lesson6.html)

OUTRO: 

```c

int main {

	int x;
	int *p;

	p = &x;
}
```

"A pointer to interger ("\*p is an interger, so p must be a pointer to an interger ")" font

O PONTEIRO \*p é integral, então o *valor atribuído* à \*p deve ser o endereço de memória de uma integral. 