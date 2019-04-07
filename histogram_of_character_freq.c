#include <stdio.h>
#include <ctype.h>

/* Write a program to print a histogram of the frequency of characters in its input. The bars can be horizontal. */

int main()
{
	char c;
	int fc[26], i, j;

	for (i = 0; i < 26; i++)
		fc[i] = 0;
	
	while ((c = getchar()) != '\n') {
		if(tolower(c) >= 'a' && tolower(c) <= 'z')
			fc[c - 'a']++;
	}

	for (i = 0; i < 26; i++) {
		printf("%c ", 'a' + i);
		for(j = 0; j < fc[i]; j++)
			putchar('-');
		putchar('\n');
	}

    return 0;
}
