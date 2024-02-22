#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

void CheckParentheses(char *str)
{
	size_t i;
	int x = 0;
	for(i=0; i<strlen(str); i++)
	{
		if(str[i] == '(')
		{
			x++;
		}
		else if (str[i] == ')' && (i - x) % 2 == 0 || str[i] == ')' && (i-x)==0)
		{
			x--;
		}

	}
	if(x!=0)
	{
		printf("Not Balanced\n");
	}
	else	
	{
	 for(i=0; i<strlen(str); i++)
        {
                if(str[i] == '[')
                {
                        x++;
                }
                else if (str[i] == ']' && (i -x)%2 == 0 || str[i] == ']' && (i-x) == 0)
                {
                        x--;
                }

        }
        if(x!=0)
        {
                printf("Not Balanced\n");
        }
	else
	{

	 for(i=0; i<strlen(str); i++)
        {
                if(str[i] == '{')
                {
                        x++;
                }
                else if (str[i] == '}' && (i -x)%2 == 0 || str[i] == '}' && (i-x) == 0)
                {
                        x--;
                }

        }
        if(x==0)
        {
                printf("Balanced\n");
        }
	else
	{
		printf("Not Balanced\n");
	}
	}
	}
}

int main()
{
char *str= "{}()";
CheckParentheses(str);
return(0);
}
