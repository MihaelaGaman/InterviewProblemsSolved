#include <stdio.h>
#include <string.h>

/**
	Write a program to "fold" long input lines into two or more lines after 
  the last non-blank character that occurs before the n-th column of input.
	Make sure your program does something smart with the very long lines and if
	there are no blanks or tabs before the specific column.
*/

#define MAX_LENGTH 80
int main()
{
	char c;
	char str[650] = "";
	char word[255];
	int char_on_line = 0, word_len = 0;
	int i;

	while((c = getchar()) != '\n') {
		if(c == ' ' || c == '\t') {
			if(word_len > 0) {
				if(char_on_line + word_len >= MAX_LENGTH) {
					strcat(str, "\n");
					char_on_line = 0;
				}
				strncat(str, word, word_len);
				char_on_line += word_len;
				word_len = 0;
				strcpy(word, "");
			}

			if(c == ' ') {
				strncat(str, " ", 1);
				char_on_line += 1;
			} else {
				strncat(str, "\t", 1);
				char_on_line += 4;
			}
		} else {
			word[word_len] = c;
			word_len++;
		}
	}

	printf("%s\n", str);

	return 0;
}
