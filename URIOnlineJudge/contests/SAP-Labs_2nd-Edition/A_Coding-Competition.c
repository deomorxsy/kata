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

    for (i=0; i < univ; i++) {
        scanf("%d", &teams[i]);
    }

    for (i=0; i < univ; i++) {
        while (teams[i] % 3 != 0) {
            //for (i=0; i<univ; i++)
            teams[i] -= 1;
        }
    }
    for (i=0; i < univ; i++){
        accumulator += teams[i];
    }

    // printf("O total de times é: %d\n", accumulator);
    return  printf("%d\n", accumulator);

}
