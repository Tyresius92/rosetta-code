#include <stdio.h>
#include <unistd.h>

int main()
{
        int c; 

        printf("How many seconds would you like to sleep?\n");
        scanf("%d", &c); 

        printf("Sleeping...\n"); 
        sleep(c); 

        printf("Awake!\n"); 
}