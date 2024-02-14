#include <stdio.h>
#include <assert.h>
#include <ex5.h>

size_t StrLen(char *str)
{
size_t length = 0;
assert(*str);
while(*str++)
{
        length++;
}
return length;
}

int StrCmp(char *str1, char *str2)
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

