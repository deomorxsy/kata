#include <stdio.h>
#include <math.h>

float mypow(float base, int exp) {
    int i;
    float pot = 1.0;

    for(i=0; i < exp; i++) {
        pot *= base;
        //printf("%d", pot);
    }

    return pot;
}

int main() { 
//Note que sem isfinite() e isnan(), R1=-nan e R2=-inf.
    float a, b, c, r1pos, r2neg, delta;

    scanf("%f%f%f", &a, &b, &c);
	delta = mypow(b, 2) - (4*a*c);
    
    //printf("%f\n", delta);

	r1pos = (-(b) + sqrt(delta)) / (2 * a);
	r2neg = (-(b) - sqrt(delta)) / (2 * a);

	//isnan retorna 1; isfinite retorna 0;
	//printf("r1pos vale %d\n", isnan(r1pos));

    if (isfinite(r1pos) != 0 &&
    	isnan(r1pos) != 1)
    {
    	printf("R1 = %.5f\nR2 = %.5f\n", r1pos, r2neg);
	
	} else {
    	printf("Impossivel calcular\n");
    }

    return 0;
}	

