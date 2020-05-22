#include <stdio.h>

//date: 2020-05-11

int main() {
    int array[] = {1, 7, 4, 5, 9, 3, 5, 11, 6, 3, 4};
    int i = 0;

    while (i < 10) {
    /* your code goes here */
        i++;
        // i should be iterated at the top of the loop
    
         if (array[i] < 5)
        {
            continue;
    }
    
    if (array[i] > 10)
    {
        break;
    }

    printf("%d\n", array[i]);
    //i++;
    }

    return 0;
}