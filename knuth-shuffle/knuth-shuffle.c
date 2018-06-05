#include <stdio.h>
#include <stdlib.h>

#define MAX_ELEMS 25

int main()
{
        int ray[MAX_ELEMS]; 

        for (int i = 0; i < MAX_ELEMS; i++) {
                ray[i] = i;
                printf("ray[%d] = %d\n", i, ray[i]); 
        }

        printf("Shuffling\n"); 

        for (int i = MAX_ELEMS; i > 0; i--) {
                int j = rand() % i;
                int temp = ray[j]; 
                ray[j] = ray[i - 1]; 
                ray[i - 1] = temp; 
        }

        for (int i = 0; i < MAX_ELEMS; i++) {
                printf("ray[%d] = %d\n", i, ray[i]);
        }
}