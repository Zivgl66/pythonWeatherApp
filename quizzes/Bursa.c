#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

int main()
{
int arr[8] = {6,12,3,5,2,4,9,1};
Bursa(arr, 8);
return(0);
}

Bursa(int *arr , size_t size)
{
	int buy = 0;
	int sell = 0;
	int profit = 0;
	int min = 0;
	int curr_p , i;
	for(i = 1; i<size; i++)
	{
		curr_p = (arr[i] - arr[min]);
		if(curr_p > profit)
		{
			buy  = min;
			sell = i;
			profit = curr_p;
		}
		else if(arr[i] < arr[min])
		{
			min = i;
		}
	}
	printf("buy index: %d\nsell index: %d\nprofit: %d\n", buy,sell,profit);

}
