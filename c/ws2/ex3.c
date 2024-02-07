#include <stdio.h>
#include <stdlib.h>

int main()
{
static int s_i = 7;
int i = 7;
int *ptr = &i;
int *ptr2 = (int *)malloc(sizeof(int));
int **ptr3;

if(ptr)
{
	ptr3 = &ptr;
}

printf("%p\n" , (void *)&s_i);
printf("%p\n" , (void *)&i);
printf("ptr: %p\n" , (void *)ptr);
printf("ad ptr: %p\n", (void *)&ptr);

printf("ptr2: %p\n" , (void *)ptr2);
printf("ptr2: %p\n" , (void *)&ptr2);

printf("ptr3: %p\n" , (void *)ptr3);


free(ptr2);


return(0);
}
