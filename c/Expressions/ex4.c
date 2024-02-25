#include <stdio.h>
//function that recives int n and returns 10^n. no pow func.


long double pow_func(int y)
{
   long double sum=1.00;
   long double xx = 10.0;
   int i;
    if (y<0){
        y=-1*y;
        xx=1/xx;
    }
    for (i=1;i<=y;i++)
    {
        sum=sum*xx;
    }

return p;
}

int main()
{
int num;
printf("enter a number to power 10: \n");
scanf("%d", &num);
long double s = pow_func(num);
printf("%ld\n", s);

return 0;
}
