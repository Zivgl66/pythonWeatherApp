#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

#define PRINTSIZE(Type) printf("sizeof " #Type " is: %ld\n", sizeof(#Type))

int main()
{
PRINTSIZE(short int);
PRINTSIZE(unsigned short int);
PRINTSIZE(unsigned int);
PRINTSIZE(int);
PRINTSIZE(long int);
PRINTSIZE(unsigned long int);
PRINTSIZE(signed char);
PRINTSIZE(unsigned char);
PRINTSIZE(float);
PRINTSIZE(double);
PRINTSIZE(long double);

return (0);
}
