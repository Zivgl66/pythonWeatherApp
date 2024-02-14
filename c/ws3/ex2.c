#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

int Josephus(int size);

int main()
{
int size;
printf("enter size of soliders: ");
scanf("%d", &size);
printf("alive solider: %d\n", Josephus(size));
return(0);
}

int Josephus(int size)
{
int *arr;
int i, count=0 , killer=0, victim = 1;
arr = malloc(size * sizeof(int));
for(i = 0; i<size; i++)
{
	arr[i] = 1;
}
while(count < size)
{
	if(arr[killer] == 1)
	{
	victim = (killer +1)  % size;
	while(arr[victim] == 0)
	{
	victim = (victim + 1) % size;
	}
	arr[victim] = 0;
	killer = victim;
	count++;
	}
	else
	{
	killer = (killer + 1) % size;
	}	
}
return killer + 1;
}

