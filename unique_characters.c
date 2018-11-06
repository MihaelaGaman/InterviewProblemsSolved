/**
Implement a function to determine if a string has all unique characters.

Solution:
	- Temporal Complexity: O(n^2)
	- Space required (additional): None
*/

static int checkUnique(char *s)
{
	int i, j;
	
	for(i = 0; i <= strlen(s); i++) {
		for (j = i + 1; j <= strlen(s); j++) {
			if (s[i] == s[j])
				return 0;
		}
	}
	return 1;
}

int main(void)
{
	// Test 1: Not unique
	//char s[] = "madnsdjnfdds";
	
	// Test 2: Unique
	//char s[] = "abcdefgsh";
	
	// Test 3: One character
	//char s[] = "a";
	
	// Test 4: Palindrome
	char s[] = "anamana";
	
	if (checkUnique(s) == 1)
		printf("Unique!\n");
	else
		printf("NOT unique!\n");
		
	return 0;
}