#include <stdio.h>

//date: 2020-05-11

int main() {
  int array[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
  int factorial = 1; // neutral element
  int i;

  for (i=0; i < 10; i++)
  {
      factorial *= array[i];
  }
  /* calculate the factorial using a for loop  here*/

  printf("10! is %d.\n", factorial);
}