/**
Write code to reverse a C-Style String 
(C-String means that “abcd” is represented as five characters, 
including the null character).
*/

static char* reverse_str(char *s)
{
	char *start, *end; 
	int len; 
	char t; 
	
	len = strlen(s); 
	
	start = s; 
	end = &s[len-1]; 
	
	while(start < end) { 
		// swap chars 
		t = *start; 
		*start = *end; 
		*end = t; 
		
		// advance pointers 
		start++; 
		end--; 
	} 
	
	return s;
}

int main(void)
{
	// Test 1: Normal string
	char s[] = "jambon";
	printf("S = %s\n", s);
	printf("Reversed s = %s\n", reverse_str(s));
	return 0;
}