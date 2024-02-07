#include <stdio.h>
#include <stdlib.h>
/*	function to swap two size_t	*/
static void SwapSizeT(size_t *a, size_t *b);
/*	function to swap two size_t pointers	*/
static void SwapSizeTP(size_t **a, size_t **b); 

int main()
{
size_t a = 10, b = 20;
size_t *ptr1 = &a, *ptr2 = &b;
/*SwapSizeT(&a , &b);*/
printf("a: %ld\n", a);
printf("a address: %p\n", (void *)&a);
printf("b: %ld\n", b);
printf("ptr1 value: %ld\n", *ptr1);
printf("ptr2 value: %ld\n", *ptr2);
printf("ptr1 address: %p\n",(void *) &ptr1);

SwapSizeTP(&ptr1, &ptr2);
printf("ptr1 value after swap: %ld\n", *ptr1);
printf("ptr2 value after swap: %ld\n", *ptr2);
printf("a value after swap: %ld\n", a);
printf("b value after swap: %ld\n", b);
return(0);
}

static void SwapSizeT(size_t *a, size_t *b)
{
size_t c = *a;
*a = *b;
*b = c;
}

static void SwapSizeTP(size_t **a, size_t **b)
{
SwapSizeT((void*)a, (void *)b);
}
