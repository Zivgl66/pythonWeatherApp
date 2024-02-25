#include <stdio.h>

int reverse_num(int n)
{
int reverse = 0, reminder;
while( n!=0)
{
reminder = n % 10;
reverse = reverse * 10 + reminder;
n = n/10;
}
return reverse;
}

int main()
{
int n, result;
printf("Enter integer: \n");
scanf("%d", &n);
result= reverse_num(n);
printf("reversed num: %d\n" , result);
return 0;
}

