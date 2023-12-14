#include <stdio.h>

//date: 22/05/2020

int sum (int num) {
/**
* find sum to n numbers	
*/
	static int var = 0;
	var += num;
	return var;
}

int main() {
	printf("%d ",sum(55));
	printf("%d ",sum(45));
	printf("%d ",sum(50));
 	
 	return 0;
}

