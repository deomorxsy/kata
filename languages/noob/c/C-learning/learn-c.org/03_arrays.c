#include <stdio.h>

//date: 20/02/2020

int main() {
    /* TODO: define the grades variable here */
    int grades[3]; // edited part
    int average;

    grades[0] = 80;
    /* TODO: define the missing grade
     so that the average will sum to 85. */
    grades[1] = 85; // edited part
    grades[2] = 90;

    average = (grades[0] + grades[1] + grades[2]) / 3;
    printf("The average of the 3 grades is: %d", average);

    return 0;
}