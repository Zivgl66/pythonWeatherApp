#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

int main()
{
char* p="lalala";
char arr[10] = "lalala";

++p;
++arr;
*p = 's';
p[0] = 's';
arr[1] = 's';
*(arr + 1) = 's';
1[arr] = 's';

return(0);
}
