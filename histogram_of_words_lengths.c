#include <stdio.h>


/**
	Write a program to print a histogram of the lengths of words in its input.
    The bars can be horizontal.
 */
int main()
{
	char c;
	
	while ((c = getchar()) != EOF) {
		if(c == '\n' || c == '\t' || c == ' ' || c == '.' || c == ',')
			putchar('\n');
		else
			putchar('-');
	}

    return 0;
}
