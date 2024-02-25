objects = foo.o foo_test.o
gd= -ansi -pedantic-errors -Wall -Wextra -DNDEBUG -O3 -o
CC= gcc
SRC= foo.c foo_test.c

mainFoo: $(objects)
	$(CC) $(gd) $@ $(objects)
	./mainFoo

$(objects) : $(SRC) foo.h
	$(CC) -c $(SRC)

.PHONY: clean
clean:
	rm mainFoo
	
