#include <stdio.h>
#include <string.h>

#define TAB_STOP 4

int main(void) 
{
	char c;
	char str[255];
	int i, j = 0;

	while((c = getchar()) != '\n') {
		if(c == '\t') {
			for(i = 0; i < TAB_STOP; i++) {
				str[j] = ' ';
				j++;
			} 
		} 
		else {
				str[j] = c;
				j++;
		}
	}	

	printf("str = %s\n", str);
	
	return 0;
}
