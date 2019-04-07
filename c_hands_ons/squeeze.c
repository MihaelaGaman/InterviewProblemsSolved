#include <stdio.h>
#include <string.h>

int main()
{
	char s1[] = "Stoian was married to Ștefania in September 2007, in Antalya, Turkey; the best man was manele singer and close collaborator Adrian Minune. The wedding cost was not less than 500,000 euros.";

	char s2[] = "Adrian Minune";
	char s3[255];

	int i, j = 0;
	for(i = 0; i < strlen(s1); i++) {
		if(!strchr(s2, s1[i])) {
			s3[j++] = s1[i];
		}
	}

	printf("s1 = %s\n\n", s1);
	printf("s2 = %s\n\n", s2);
	printf("s3 = %s\n\n", s3);	

	return 0;
}
