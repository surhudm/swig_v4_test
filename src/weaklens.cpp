#include <iostream>
#include "weaklens.h"

weaklens::weaklens(int h, int b){
    printf("%d %d\n", h, b);
}

weaklens::~weaklens(){
}

int weaklens::test(int h, int b){
    printf("h:%d b:%d \n", h, b);
    return 1;
}

/*
int main(){
weaklens();
}
*/
