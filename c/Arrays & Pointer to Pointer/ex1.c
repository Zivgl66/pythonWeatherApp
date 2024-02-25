#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#define M 2
#define N 3


/*	1st way		
const int M = 3;
const int N = 3;
void print(int arr[M][N	]);
print(arr);

      2nd way        
void print(int m, int n, int arr[][n]);
print(m,n,arr);

      3rd way         
void print(int arr[][N], int m );
print(arr,3);

      4th way         
void print(int *arr, int m, int n);
print((int *)arr, m, n);

      5th way         
void print(int (*arr)[M]); 
print(arr);
*/

/* calculate sum of each row in a mtrix */
void SumMatrixValues(int matrix_array[M][N], int result_arr[M]);

int main()
{

int two_d_arr[M][N] = { {1,2,3} , {4,5,6} };
/*int multi_arr[10][20];*/
int result_arr[M];
int i;

/* access specific location in array 	
printf("value: %d\n", two_d_arr[0][1]);

 sizeof two dimensional array		
printf("sizeof two: %ld\n", sizeof(two_d_arr) / sizeof(two_d_arr[0][0]));
printf("sizeof multi: %ld\n", sizeof(multi_arr) / sizeof(int));
*/
SumMatrixValues(two_d_arr ,result_arr);

for(i = 0; i < 2; i++)
{
printf("result of row %d: %d\n",i, result_arr[i]);
}


return(0);
}


void SumMatrixValues(int matrix_array[M][N], int result_arr[M])
{
int sum = 0;
int i, j;

for(i = 0; i < M; i++)
{
	for(j = 0; j < N; j++)
	{
	sum+= matrix_array[i] [j];
	}
	result_arr[i] = sum;
	sum = 0;
}
}
