#include <stdio.h>
#include <assert.h>
size_t StrLen(const char *str);
int StrCmp(const char *str1,const char *str2);

int main()
{
char a[6]="HELL";
char b[12]="HELLO";
char c[8]="Hellooo";
char d[6]="HeLlo";
printf("the length of the string is: %lu\n", StrLen(a));
printf("strcmp(a, b) = %d\n", StrCmp(a,b));
printf("strcmp(a, c) = %d\n", StrCmp(a,c));
printf("strcmp(c, d) = %d\n", StrCmp(c,d));
return(0);
}

size_t StrLen(const char *str)
{
	size_t length = 0;
	assert(*str);
	while(*str++)
	{
		length++;
	}
	return length * sizeof(char);
}

int StrCmp(const char *str1,const char *str2)
{
assert(*str1);
assert(*str2);
while(*str1)
{
	if(*str1 > *str2)
	{
	return 1;
	}
	if(*str2 > *str1)
	{
	return -1;
	}
	str1++;
	str2++;
}
if(*str2 != '\0')
	{
	return -1;
	}
else
	{
	return 0;
	} 
}
