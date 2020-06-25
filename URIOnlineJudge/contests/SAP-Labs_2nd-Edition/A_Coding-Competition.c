#include <stdio.h>

int univ_number() {
    int number = 1;
    scanf("%d", &number);

    return number;
}

int main() {
    int univ = univ_number();
    int teams[univ];
    int i, accumulator= 0;
    
    //loop to assign values to each item/index of teams[i].
    //Doesn't work without the Adress Operator "&". 
    for (i=0; i < univ; i++) {
        scanf("%d", &teams[i]);
    }

    // loop to create the maximum number of teams of three to each college. 
    for (i=0; i < univ; i++) {
        while (teams[i] % 3 != 0) {
            teams[i] -= 1;
        }
    }

    //loop to the summation that at each iteration assigns the index of teams to the accumulator variable. 
    for (i=0; i < univ; i++){
        accumulator += teams[i];
    }

    return  printf("%d\n", accumulator);

}

