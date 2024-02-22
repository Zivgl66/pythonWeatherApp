#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include "ex1.h"

int main()
{

pstack s1;
int s;
int i = 1;


s = PushStack(&s1, &i);
printf("success or fail: %d\n",s);

/*PeekStack(&s1);*/

return(0);
}
