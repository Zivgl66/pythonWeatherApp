#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include "g.h"

int main()
{
printf("%d\n", g_s);
Foo();
printf("%d\n", g_s);
return(0);
}
