/*
CR: Dennis;
*/

#include <stdio.h>	
#include <stdlib.h>	/*uses size_t*/
#include <string.h>	/*uses malloc function*/ 
#include "stack.h"	/*Stack functions header*/

struct Stack{
	void *arr;
	size_t stack_size;
	size_t element_size;
	size_t stack_capacity;
};

int main()
{
struct Stack *s;
char str1[] = {"h""e""y""\0"};
char *str;
int sre = 2132321;
int *sr;
s = CreateStack(100,8);
PushStack(s, str1);
PushStack(s, "hello");
PushStack(s , &sre);
printf("is stack empty? %d\n", IsEmptyStack(s));
PopStack(s);
str = PeekStack(s);
printf("element in stack is: %s\n", str);
printf("stack capacity: %ld\n", CapacityStack(s));
printf("stack size: %ld\n", SizeStack(s));
PopStack(s);
printf("is stack empty? %d\n", IsEmptyStack(s));
DestroyStack(s);
return(0);
}

/* Create a new stack using it's entered cpacity and the size of each element */
struct Stack* CreateStack(size_t cap, size_t size)
{
	struct Stack *new_stack = malloc(sizeof(*new_stack));
	new_stack->arr =malloc(cap*size);
	if(new_stack->arr == NULL)
	{
		printf("malloc failed");
	}
	new_stack-> element_size= size;
	new_stack-> stack_size = 0;
	new_stack-> stack_capacity = cap;
	return new_stack;
}

/* free the space in memeory of the array of the stack and the pointer*/
void DestroyStack(struct Stack *s)
{
	free(s->arr);
	free(s);
	s = NULL;
}

/* decrement 1 from the stack size, losing the pointer to that element*/
void PopStack(struct Stack *s)
{
	
	s->stack_size--;
}
/*check if there is a place in the stack, if so, copy the memory address of the new element, with the acceptable size of element in the stack to the last place in the array*/
void PushStack(struct Stack *s, void *new_elm)
{
	if(s->stack_size >= s->stack_capacity)
	{
		printf("stck is at it's capacity\n");
	}
	else
	{
	memcpy((char *)s->arr + s->stack_size * s->element_size , new_elm, s->element_size);
	s->stack_size++;
	}
}
/* declare a temporary pointer and copy the last element in the stack to it's value*/
void * PeekStack(const struct Stack *s)
{
	void *tmp = malloc(s->element_size);
	memcpy(tmp,(char *)s->arr + (s->stack_size - 1) * s->element_size, s->element_size);
	return tmp;
}
/* return the current stack size*/
size_t SizeStack(const struct Stack *s)
{
	return s->stack_size;
}

/* check if the stack is empty*/
int IsEmptyStack(const struct Stack *s)
{
	if(s->stack_size == 0)
	{
		return 0;
	}
	else
	{
		return 1;
	}
}

/* return the stack capacity */
size_t CapacityStack(const struct Stack *s)
{
	return s->stack_capacity;
}


