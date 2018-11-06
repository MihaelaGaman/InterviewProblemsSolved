/**
Write a method to replace the spaces in a string with '%20'.
*/

void replace_spaces(char *s)
{
	int i = 0, last_space = 0;
	char *t;
	char aux[100];
	
	t = s;
	
	while(i < strlen(s)) {
		if (*t == ' ') {
			if(strlen(aux == 0))
				strcpy(aux, s, i-1);
			else
				strncat()
		}
		t++;
		i++;
	}
	printf("Out\n");
	printf("%s\n", s);
	//return s;
}

int main(void)
{
	char s[] = "Ana are mere.";
	replace_spaces(s);
	printf("New string: %s\n", s);
	
	return 0;
}