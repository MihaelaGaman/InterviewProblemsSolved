#include <stdio.h>
#include <string.h>

/**
	Return the first location in string s1 where any of the character in string s2 occurs or -1 if there are no characters in s1 from s2.
	Note strpbrk does the same, but it returns a pointer.
*/

int main()
{
	char s1[] = "Stoian was married to Ștefania in September 2007, in Antalya, Turkey; the best man was manele singer and close collaborator Adrian Minune. The wedding cost was not less than 500,000 euros.";

	char s2[] = "Adrian Minune";

	int i, j = -1;
	for(i = 0; i < strlen(s1); i++) {
		if(strchr(s2, s1[i])) {
			j = i;
			break;
		}
	}

	if(j == -1)
		printf("None of the characters in s2 was found in s1!\n");
	else
		printf("The first matching character is at pos = %d\n", j);

	return 0;
}
