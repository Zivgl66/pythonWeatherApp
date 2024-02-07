/* a function to copy an array [int] */

#include <stdio.h>
/*	a function to copy an array of integers into another array */
void CopyArray(int size,int *arr1, int *arr2);

int main()
{

int array1[]={1,2,3,4,5};
int array2[5];
int size, i;
size = sizeof(array1) / sizeof(array1[0]) - 1;

CopyArray(size,array1,array2);

for(i=0; i<=size; i++)
{
printf("%d\n" , array2[i]);
}

return (0);
}


void CopyArray(int size,int *arr1, int *arr2)
{

int i;

for(i = 0; i<= size; i++)
{
	arr2[i] = arr1[i];
}

}
