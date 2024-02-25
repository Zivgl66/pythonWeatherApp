#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

#define SIZEARR 57

/*	A Function to Convert String to lower case	 */
void ConvertStrToLower(char *str);
/*      A Function to Convert an Array of strings to lower case       */
void ConvertArrToLower(char **arr);
/*      A Function to Copy a string array into an empty array       */
void CopyStrArr(char **arr, char **copyArr);

int main(int argc, char *argv[], char *envp[])
{

char *copyArray[SIZEARR];
int i;

ConvertArrToLower(envp);
CopyStrArr(envp, copyArray);

for(i = 0; i < SIZEARR; i++)
{
printf("%s\n" , copyArray[i]);
}

return(0);
}

void ConvertStrToLower(char *str)
{
unsigned long int i;
for(i = 0;i< strlen(str); i++)
{
	if(str[i] >= 65 && str[i] <= 90)
	{	
		str[i] = str[i] + 32;
	}
}
}

void ConvertArrToLower(char **arr)
{
while(*arr != NULL)
{
ConvertStrToLower(*arr++);
}
}

void CopyStrArr(char **arr, char **copyArr)
{
while(*arr != NULL)
{
*copyArr++ = *arr++;
}
}





