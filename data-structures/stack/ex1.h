#ifndef STACK_H
#define STACK_H

typedef struct Stack {
        void *data;
	struct Stack *next;
} *pstack;

int CreateStack(pstack *s);
int DestroyStack(pstack *s);
int PopStack(pstack *s);
int PushStack(pstack *s, void *new_elm);
int PeekStack(pstack *s);
int SizeStack(pstack *s);
int IsEmptyStack(pstack *s);
int CapacityStack(pstack *s); 

#endif
