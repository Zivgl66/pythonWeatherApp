#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include "ex1.h"

/*
int CreateStack(pstack *s)
{
}
*/

int IsEmptyStack(pstack *s)
{
	if((*s)->data == NULL)
	{
		return 0;
	}
	return -1;
}

int DestroyStack(pstack *s)
{
	while(IsEmptyStack(s) != 0)
	{
		PopStack(s);	
	}
}

int PopStack(pstack *s)
{
	struct Stack *tmp;
	void *i;
	if(IsEmptyStack(s) == 0)
	{
		return -1;
	}
	tmp = *s;
	i = (*s)->data;
	*s = (*s)->next;
	free(tmp);
	printf("poped: %p\n", i);
	return 0;
}

int PushStack(pstack *s, void *new_elm)
{
	pstack *current = (pstack *)malloc(sizeof(pstack));
	printf("the new item is: %p\n", (void *)new_elm);
	if(!current)
	{
		return -1;
	}
	(*current)->data = new_elm;
	(*current)->next = *s;
	s = current;
	printf("item added to stack\n");
	return 0;
}

int PeekStack(pstack *s)
{
	if(IsEmptyStack(s) == 0)
	{
		printf("stack is empty");
		return -1;
	}
	printf("Top element in stack: %p", (*s)->data);
	return 0;
}

int SizeStack(pstack *s)
{
	int counter = 0;
	if(IsEmptyStack(s) == 0)
        {
                printf("stack is empty");
                return -1;
        }
	while(s++)
	{
		counter++;
	}
	printf("Stack size: %d", counter);
	return 0;
}

/*
int CapacityStack(pstack *s)
{	
}
*/

