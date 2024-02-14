#include <stdio.h>

int FindDuplicate(int *arr, int size);

int main()
{
int arr[10]={1,2,2,1,3,4,3,2,3,3};
printf("unique number is: %d \n",FindDuplicate(arr, 10));
return(0);
}

int FindDuplicate(int *arr, int size)
{
int i,j ,temp;
int counter = 1;
for(i=0; i<size; i++)
    {
        for(j=i+1; j<size; j++) 
	{
		if(arr[i]>=arr[j])
           	{
               		temp = arr[i];
                	arr[i] = arr[j];
                	arr[j] = temp;
		}
        }
    }
for(i=0; i<size; i++)
{
printf("array in place %d: %d\n", i , arr[i]);
}
temp = arr[0];
for(i=0; i<size; i++)
{
	if(temp == arr[i+1])
	{
		counter++;
	}
	else if(temp != arr[i+1] && counter == 1)
		{
			return temp;
		}
	else 
	{
		temp = arr[i+1];	
		counter = 1;
	}
}
}

