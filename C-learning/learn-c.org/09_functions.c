#include <stdio.h>

//date: 18/05/2020

/* function declaration */
void print_big(int x);

int main() {
  int array[] = { 1, 11, 2, 22, 3, 33 };
  int i;
  for (i = 0; i < 6; i++) {
	print_big(array[i]);
  }
  return 0;
}

/* write your function here */
void print_big(int x) {
	if (x > 10) {
		printf("%d is big\n", x);
	}
}