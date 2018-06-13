#include <stdio.h>

const int OPEN = 1; 
const int CLOSED = 0; 
const int NUM_DOORS = 100; 

int main()
{
        int ray[NUM_DOORS]; 

        for (int i = 0; i < NUM_DOORS; i++) {
                ray[i] = CLOSED; 
        }

        fprintf(stderr, "Made it here\n"); 

        for (int i = 1; i <= NUM_DOORS; i++) {
                for (int j = 1; j <= NUM_DOORS; j++) {
                        if ((i % j) == 0) {
                                if (ray[i - 1] == CLOSED) 
                                        ray[i - 1] = OPEN;
                                else
                                        ray[i - 1] = CLOSED;
                        }
                }
        }

        for (int i = 0; i < NUM_DOORS; i++) {
                if (ray[i] == OPEN) 
                        printf("Door %3d: Open\n", i + 1);
                else
                        printf("Door %3d: Closed\n", i + 1);
        }
}