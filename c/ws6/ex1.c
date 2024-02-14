#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
/*
void Print(int num);
typedef struct print_me {
int p;
void (*Print)(int p);
};

int main()
{
struct print_me prints[10];
int i;

for(i=0; i<10; i++)
{
prints[i].p = i;
prints[i].Print = Print;
}

for(i=0; i<10; ++i)
{
prints[i].Print( prints[i].p );
}

return(0);
}


void Print(int num)
{
printf("int value: %d\n", num);
}
*/

struct print_me {
int value;
void (*ptrPrint)(struct print_me *);
};

void Print(struct print_me *p)
{
printf("value: %d\n", p->value);
}

int main()
{
struct print_me prints[10];
int i;
for(i=0; i<10; i++)
{
prints[i].value = i;
prints[i].ptrPrint = &Print;
}
for(i=0; i< 10; i++)
{
prints[i].ptrPrint(&prints[i]);
}
return (0);
}


