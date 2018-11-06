/**
	Write a method to decide if two strings are anagrams or not.
*/

static int are_anagrams(char *s, char *t)
{
	int i, j;
	int found = 0;
	
	for (i = 0; i <= strlen(s); i++) {
		for (j = 0; j <= strlen(t); j++) {
			if (t[j] == ' ')
				break;
			if (s[i] == t[j]) {
				found ++;
				break;
			}
		}
	}
	
	if(found < strlen(t))
		return 0;
		
	return 1;
}

int main(void)
{
	/* Test with anagrams*/
	//const char *anagrams_s[] = {"restful", "rail safety", "funeral", "adultery"};
	//const char *anagrams_t[] = {"fluster", "fairy tales", "real fun", "true lady"};
	
	/* Test with non anagrams */
	const char *anagrams_s[] = {"rested", "rail safety", "funeral", "adultery"};
	const char *anagrams_t[] = {"fluster", "fairy talezz", "really funny", "true lady-ish"};
	int i;
	
	int n_array = (sizeof (anagrams_s) / sizeof (const char *));
	
	for(i = 0; i < n_array; i++) {
		if(are_anagrams(anagrams_s[i], anagrams_t[i]))
			printf ("%s   and   %s   are ANAGRAMS!\n", anagrams_s[i], anagrams_t[i]);
		else
			printf ("%s   and   %s   are NOT ANAGRAMS!\n", anagrams_s[i], anagrams_t[i]);		
	}
	
	return 0;
}