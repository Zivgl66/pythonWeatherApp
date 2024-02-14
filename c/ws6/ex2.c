#include <stdio.h>
#include <assert.h> /* used to assert file exists */
#include <stdlib.h>
#include <string.h>  /* used for strcmp function */

/*
psuedocode:
A Program to modify files:

	The program recieves file name as an argument.
	
	Before the main function, we declare a struct which includes a string and two function's pointers.
	We also decalre an array of structs with the operation and name of operation hardcoded.
	We decalre an enum for the return type of the operation function.

	In main, we invoke a function with the file name.
		

		The Center Function - (file_name)
		-Check if file exits, using assert.
		-Echo the options for the user.
		-Scan for user input.
		-A loop starts while user input doesnt equal 'exit'.
		-Iterate over the array of structs.
		-Invoke each struct comparison function, comparing for the user input.
		-Invoke matching struct's operation function.
		-If NO match found, append the user's input to end of file.
		-If user input equals 'exit' , break and abort program.
		
		Compare function - (operation_name, user_input)
		-Use 'strcmp' function to compare the two strings.
		-If there is a match Return 1.
		-If no match found Return 0.
		
		
		Operations Functions:

		Remove function - (file_name)
		-Open file using 'fopen' function.
                -Check if file was successfully opened, if not return an error.
		-Close file using 'fclose' function.
		-Remove file useing 'remove' function.
		-Print "file was deleted" to the user.
		-Return.


		CountLines function - (file_name)
		-Declare an int count variable initialized to 0.
		-Declare a char variable to store character from file.
		-Open the file using 'fopen' function.
                -Check if file was successfully opened, if not return an error.
		-Extract characters from file and store in char variable.
		-Increment count variable if this character is a newline (\n).
		-Close the file using 'fclose' function.
		-Print the number of lines in the file (counter) to the user.
		-Return.

		Exit:	
		-If user input equals exit - abort.

		--Returns an enum, recieves file_name and string user_input as arguments--
		AppendToEnd function - (file_name, user input)
		-Open the file using 'fopen' function in append mode (using "a" argument).
		-Check if file was successfully opened, if not return an error.
		-If opened successfully, use 'fprintf' function to print user input to the file.
		-Close thefile using 'fclose' function.
		-Return.


		AppendToStart function - (file_name, user input)
		-Open the file using 'fopen' function in append mode (using "a" argument).
		-Check if file was successfully opened, if not return an error.
		-Create a new file and name it 'temp', append to temp new user input.
		-Copy all of the original's file text to a variable.
		-Append the original file text to the end of the temp file.
		-Delete the original file using the delete function.
		-Rename the temp file to the original file's name.
		-Return.

*/
#define KRED  "\x1B[31m"
#define KNRM  "\x1B[0m"
#define KGRN  "\x1B[32m"


typedef enum State {Working = 1, Failed = 0} State;
State work = Working;

void CenterFunction(const char *filename);
void PrintMenu();

int Compare(const char *str1, const char *str2);
State RemoveFile(const char *filename);
State CountFileLines(const char *filename);
State Exit();
State AppendToFile(const char *filename,const char *input);
State PrependToFile(const char *filename,const char *input);


typedef struct Logger {
	char *name;
	int (*func_cmp)();
	State (*func_op)();
}Logger;

struct Logger logger_array[4] = {
{"-remove" , Compare, RemoveFile},
{"-count" , Compare, CountFileLines },
{"-exit" , Compare , Exit},
{"<", Compare , PrependToFile}
};

char *menu[100]={"To remove a file enter: '-remove'", "To Count lines enter: '-count'", "To Exit enter: '-exit'", "To Append text to start use: '<'", "To append text enter any input"}; 

int main(int argc, char **argv)
{
	if(argc > 1)
	{
		CenterFunction(argv[1]);
	}
	else
	{
		printf("%s", KRED);
		printf("No file was entered.\n");
		printf("%s", KRED);

	}
	return(0);
}

void CenterFunction(const char *filename)
{
	int i;
	int match;
	char input[100];
	FILE *fp = fopen(filename, "r+");
	if(fp != NULL)
	{
		fclose(fp);
		while(work == Working)
		{
			match = -1;
			PrintMenu();
			if(fgets(input, 99, stdin) != NULL)
			{
				if ((strlen(input) > 0) && (input[strlen (input) - 1] == '\n'))
				{
			       	input[strlen (input) - 1] = '\0';
				}
			}
			for(i = 0; i < 4; i++)
			{
				if(logger_array[i].func_cmp(logger_array[i].name , input) == 0)
				{
					match = i;
				}
			}			
			if(match != -1)
			{
				work = logger_array[match].func_op(filename);
			}	
			else
			{
				work = AppendToFile(filename, input);

			}
		}
	}
	else
	{
		printf("%s", KRED);
		printf("Could not open the file!\n");
		printf("%s",KNRM);
	}
}

void PrintMenu()
{
	int i;
	printf("\n");
	for(i = 0; i < 5; i++)
	{
        	printf("%s\n", menu[i]);
        }
	printf("\n");
}

int Compare(const char *str1, const char *str2){
	if(str2[0] == '<')
	{
		return 0;
	}
	else
	{
        	return strcmp(str1,str2);
	}
}

State RemoveFile(const char *filename)
{
	FILE *fp;
	fp = fopen(filename, "r");
	if(fp == NULL)
	{
        	printf("Could not open file\n");
		return Failed;
	}
	if(remove(filename) == 0)
	{
		printf("Deleted successfully\n");
	}
	else
	{
        	printf("Unable to delete the file\n");
		return Failed;
	}
	fclose(fp);
	return Working;
}

State CountFileLines(const char *filename)
{
	FILE *fp;
	int counter = 0;
	char c;
	fp = fopen(filename, "r");
	if(fp == NULL)
	{	
		printf("Could not open file\n");
		return Failed;
	}

	for (c = getc(fp); c != EOF; c = getc(fp))
	{       
		if (c == '\n')
		{ 
        		counter++;
		}
	}
	fclose(fp);
/*	printf("The File", "%s",KGRN,"%s",filename,"%s",KNRM," has", "%s",KRED," %d", counter, "%s",KNRM, " lines\n");*/
	printf("The file ");
	printf("%s", KGRN);
	printf("%s", filename);
	printf("%s", KNRM);
	printf(" has ");
	printf("%s", KRED);
	printf("%d", counter);
	printf("%s", KNRM);
	printf(" lines\n"); 
	return Working;
}

State Exit()
{
	printf("exiting program \n");
	return Failed;
}

State AppendToFile(const char *filename,const char *input)
{
	FILE *fp;
	fp = fopen(filename, "a+");
	if(fp == NULL)
	{
        	printf("Could not open file\n");
	        return Failed;
	}
	fprintf(fp,"%s", "\n");
	fprintf(fp,"%s", input);
	fclose(fp);
	printf("added: %s \nto end of file\n", input);
	return Working;
}

State PrependToFile(const char *filename,const char *input)
{
	char *text = NULL;
	FILE *fp;
	size_t file_size = 0;
	char line[128];
	input++;
	fp = fopen(filename, "r+");
	if(fp == NULL)
	{
        	printf("Could not open file\n");
	        return Failed;
	}
	while (fgets(line,sizeof(line),fp))
	{
		file_size+=strlen(line);
		strcat(text=realloc(text,file_size),line);
	}
	rewind(fp);
	fprintf(fp,"%s", input);
	fprintf(fp,"%s", "\n");
	fprintf(fp,"%s", text);
	free(text);
	fclose(fp);
	printf("added: %s \nto start of file\n", input);
	return Working;
}

