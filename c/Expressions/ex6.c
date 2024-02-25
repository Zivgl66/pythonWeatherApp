#include <stdio.h>
//function the swaps values of 2 variables.

//solution 1
void swap_vals(int *x, int *y)
{
int z = *y;
*y = *x;
*x = z;
}

//solution 2
void swap2_vals(int *x, int *y)
{
*x = *x + *y;
*y = *x - *y;
*x = *x - *y;
}

//solution 3
void swap3_vals(int *x, int *y)
{
*x = *x ^ *y;
*y = *y ^ *x;
*x = *x ^ *y;
}

int main()
{
int x , y;
printf("enter a number: \n");
scanf("%d" , &x);
printf("enter a second number: \n");
scanf("%d", &y);
//swap_vals(&x,&y);
//swap2_vals(&x,&y);
swap3_vals(&x,&y);

printf("x is now: %d\n", x);
printf("y is now: %d\n", y); 
return 0;
}
