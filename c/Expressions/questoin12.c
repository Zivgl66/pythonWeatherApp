#include <stdio.h>

long l = 8;
long *foo(){ return &l;}

int main()
{
long *ptr = &l;
printf("ptr address: %ld\n",*ptr);
printf("l address: %p\n", &l);

//*(foo()) = 5;
//printf("%ld\n", l);
return(0);
}
