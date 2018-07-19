#include <stdbool.h>
#include <stdio.h>

const int TARGET = 269696;

int main()
{
        bool found = false; 
        int i = 1; 
        int squared = 0; 

        while (!found) {
                squared = i * i; 

                if (squared % 1000000 == TARGET) {
                        found = true; 
                }

                i++;
        }

        printf("Answer: %d\n", i); 
        printf("%d * %d = %d\n", i, i, squared); 
}