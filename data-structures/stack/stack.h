#include <stdio.h>
#ifndef STACK_H
#define STACK_H

typedef struct Stack Stack;

struct Stack* CreateStack(size_t stack_capacity, size_t size);
void DestroyStack(struct Stack *s);
void PopStack(struct Stack *s);
void PushStack(struct Stack *s, void *new_elm);
void * PeekStack(const struct Stack *s);
size_t SizeStack(const struct Stack *s);
int IsEmptyStack(const struct Stack *s);
size_t CapacityStack(const struct Stack *s);

#endif

