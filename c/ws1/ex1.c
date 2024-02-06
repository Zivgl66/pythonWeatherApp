#include <stdio.h>
int main()
{
//solution 1:
char hex[]="\x22\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x22";
printf("%s\n" , hex);

//solution 2:
char *hexString[] = {"22","48","65","6c","6c","6f","20","57","6f","72","6c","64","22"};
char character;
int hexValue, i;

for(i = 0; i< 13; i++)
{
sscanf(hexString[i], "%x" , &hexValue);
character = (char)hexValue;
printf("%c" , character);
}
return 0;
}
