#include <stdio.h>

void modify(int* ptr, int value) {
    *ptr = value;
}

void allocateAndModify(int** ptr) {
    *ptr = malloc( sizeof(int) );  
    **ptr = 10;
}

void cleanup(int* ptr) {
    free(ptr);  
}

int main() {
    int* ptrA = NULL;  
    int* ptrB = NULL; 
    
    printf("%p\n", ptrA);  // print (nil)
    printf("%d\n", *ptrB); // print undefined

    allocateAndModify(&ptrA);  
    printf("%d\n", *ptrA); // print 10

    modify(ptrA, 50);  
    printf("%d\n", *ptrA); // print 50

    cleanup(ptrA);  
    printf("%p\n", ptrA);  // print adress
    printf("%d\n", *ptrA); // print undefined
    ptrA = NULL;  
    printf("%p\n", ptrA);  // print (nil)
}