#include <stdio.h>
#include <string.h>

#define TAB_STOP 4


/**
 Write a program that replaces strings of blanks by the minimum number of tabs 
 and blanks to achieve the same spacing.
*/

int main(void) 
{
	char c;
	char str[255];
	int i, count_sp = 0, j = 0;

	while((c = getchar()) != '\n') {
		if(c == ' ') {
			count_sp++;
			if(count_sp == TAB_STOP) {
				str[j] = '\t';
				j++;
				count_sp = 0;
			} 
		} else {

			if(count_sp > 0) {
				for(i = 0; i < count_sp; i++) {
					str[j] = ' ';
					j++;
				}
				count_sp = 0;
			} 
			str[j] = c;
			j++;
		}
	}	

	printf("%s\n", str);
	
	return 0;
}
