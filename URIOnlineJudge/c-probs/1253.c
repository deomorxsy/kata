#include <stdio.h>
#include <string.h>
int main() {
	//char alphabet_char[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '\0'};
	char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char finder = ""; // percorrerá alphabet[]
	char accumulator[51];

	int testes = 0; // N

	char encoded[51] = "sowat";
	//char decoded[51] = "ssup";

	int right_shift = 0; /* number of right shifts the cipher will perform 
	//the input with the line of encoded characters will have a maximum of 50 characters,  \
	but the last one of a string, in C, is NULL(0).*/
	int i; //index1
	int index = 0; //index2
	int item = 0; //index3

	//scanf("%d %s %d", &tests, &encoded, &right_shift);
	//printf("tests=%d\nencoded=%s\nright_shift=%d\n", tests, encoded, right_shift);

	//printf("Alphabet:\n%s\n", alphabet);
	//printf("Alphabet variable length:%d\n%s\n", strlen(alphabet), alphabet);

	scanf("%d %s %d", &testes, &encoded, &right_shift);
	
	for (i=0; index<=testes; i = i + 1) {
		for (index=0;index <= strlen(encoded); index = index + 1) {
			encoded[index] = &finder; 
			for (item=0; item<=strlen(alphabet); item = item + 1) {
				if (finder == alphabet[item]) {
					accumulator = alphabet[item + right_shift];
					//coloca a letra destacada em accumulator
				} 
			}
		}
	}
	
	printf("%s\n", accumulator);

	//printf("i=%d\nindex=%d\nitem=%d", i, index, item);
	return 0;
	}