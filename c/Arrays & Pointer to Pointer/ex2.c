#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

int Josephus(int size);

int main()
{
int size;
/* 	Get number of soliders from the user */
printf("enter size of soliders: ");
scanf("%d", &size);
/*	Print to the user the number of the solider left alive, send the size of soliders to the function */
printf("alive solider: %d\n", Josephus(size));
return(0);
}

int Josephus(int size)
{
/*	declare an array for the soliders */
int *arr;
/*	declare variables to use, i for the for loops, count to count number of dead soliders, killer to know which 
soliders turn it is to kill and victim to know which solider's turn it is to die */
int i, count=0 , killer=0, victim = 1;
/*	allocate memory to the array with the size from the user */
arr = malloc(size * sizeof(int));
/*	initialize every element in the array with 1 = alive*/
for(i = 0; i<size; i++)
{
	arr[i] = 1;
}
/*	while the count of dead soliders isnt more than the size of the array, continue*/
while(count < size)
{
/*	if the killer is alive, search for it's next victim*/
	if(arr[killer] == 1)
	{
	victim = (killer +1)  % size;
/*	if the next victim is dead, go to the next inline*/
	while(arr[victim] == 0)
	{
	victim = (victim + 1) % size;
	}
/*	kill the victim that was alive, 0 = dead*/
	arr[victim] = 0;
/*	killer = the spot of the dead solider, search for the next killer inline*/
	killer = victim;
/*	raise the count of dead soliders by 1*/
	count++;
	}
	else
	{
/*	raise the killer by 1 place if the next inline killer is dead = 0*/
	killer = (killer + 1) % size;
	}	
}
/*	if only 1 left alive, return it's value*/
return killer + 1;
}

