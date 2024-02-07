#include <stdio.h>

int main()
{
int abcsada;
size_t i =4;
size_t array[]={5,3,7,9,10,12};
printf("%lu\n", *(i + array));
printf("%lu\n", *(array + i));
printf("%lu\n", ((size_t)3)[array]);
printf("%d", abcsada);
return (0);
}
