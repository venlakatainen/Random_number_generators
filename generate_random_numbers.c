#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    
    int i;
    time_t t;
    
    /* initialize random number generator */
    
    srand((unsigned) time(&t));

    
    for (i=0; i<100; i++){
        printf("%d\n", rand());
        
    }

    return(0);
}
