#include <stdio.h>

int main()
{
int a, b, c;
a=10, b=20, c=0; // original code
c = a++ + a++ + b++ + b++ + ++a + ++b;
printf("%d %d %d\n", a, b, c);
a=10, b=20, c=0; // sequence of sub-expressions reversed
c = ++b + ++a + b++ + b++ + a++ + a++;
printf("%d %d %d\n", a, b, c);
}
