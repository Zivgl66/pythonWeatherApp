#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

void TF(int num);
void ReverseString(char *str);

int main()
{
char str[20]="HellO WoRLd";
ReverseString(str);
TF(4);
return(0);
}

void TF(int num)
{
int i;
if(num==3) printf("T\n2\n1\n");
else if(num==2) printf("2\n1\n");
else if(num ==1) printf("1\n");
else
{
for(i =1; i<=num; i++)
{
if(num % 3 == 0) printf("T\n");
else if(num % 5 == 0) printf("F\n");
else if(num % 3==0 && num % 5 ==0) printf("TF\n");
else printf("%d\n",num);
}
}
}


void ReverseString(char *str)
{
int i;
for(i= strlen(str); i >= 0; i--)
{
if(str[i] >= 65 && str[i] <= 90)
{
str[i] = str[i] + 32;
}
printf("%c", str[i]);
}
printf("\n");
}
