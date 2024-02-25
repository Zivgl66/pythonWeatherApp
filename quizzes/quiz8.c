#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

void IsSum(int *arr, int sum, int size);

int main()
{
int arr[5] = {2, 4,8,12,14};
IsSum(arr, 21, 5);
return(0);
}

void IsSum(int *arr, int sum , int size)
{
int left = 0;
int right = size - 1;
int found = 0;

	while(left < right)
	{
		if(arr[left] + arr[right] == sum)
		{
			found = 1;
			left++;
		}
		else if(arr[left] + arr[right] < sum)
		{
			left++;
		}
		else
		{
			right--;
		}
	}
	if(found == 1)
	{
		printf("found!: %d", found);
	}
	else
	{
		printf("not found!");
	}
}
