#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print_bits(int no)
{
	int i;

	for(i = 31; i >= 0; i--) {
		printf("%d", ((no & (1 << i)) ? 1 : 0));
	
	}

	printf("\n");
}

int convert_bits_to_int(char *bits_str)
{
	int no = 0;
	for(int i = 0; i < strlen(bits_str); i++) {
		no += (bits_str[i] == '1' ? 1 << (strlen(bits_str) - i) : 0);
	}	

	return no;
}


/**
 * NOTE: strrev does not seem to be available in Linux.
 */
char *strrev(char *str)
{
	char *p1, *p2;

	if (! str || ! *str)
    	return str;
    for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2) {
   		 *p1 ^= *p2;
   		 *p2 ^= *p1;
   		 *p1 ^= *p2;
    }
    
	return str;
}

/**
 * Exercise 5.1.
 * You are given two 32 bits numbers N and M, and two bits positions, i and j.
 * Write a method to set all bits between i and j in N equal to M
 * (e.g. M becomes a substring of N located at i and staring at j).
 *
 * Example:
 * Input: N = 10000000000, M = 10101, i = 2, j = 6
 * Output: N = 10001010100
 *
 */

void set_bits_in_interval(char *n_str, char *m_str, int i, int j)
{
	int M = convert_bits_to_int(m_str);
	int N = convert_bits_to_int(n_str);
	int compl = ~1;

	printf("Exercise 5.1.\n");	
	printf("M = %d, N = %d\n", M, N);

	M = (M << i) & (compl >> (31 - j));
	N |= M;

	print_bits(N);
}

/**
 * Exercise 5.2.
 * Given a decimal number, e.g. 3.72, that is passed in as a string, print
 * the binary representation. If the number cannot be represented accurately in 
 * binary, print "ERROR".
 *
 * SOLUTION:
 * n = 0.101 = 1 * (1/2^1) + 0*(1/2^2) + 1*(1/2^3)
 *
 * To print the decimal part, we can multiply by 2 and check if 2*n is greater
 * than or equal to one. This is a "shifting" of the fractional sum.
 * r = 2 * n = 2 * 0.101 = 1 * (1/2^0) + 0 * (1/2^1) + 1 * (1/2^2) = 1.01
 *
 * if r >= 1 => n had a 1 right after the decimal point.
 * by doing this continuously, we can check every digit.
 */
void print_binary(char *n)
{
	int int_part;
	double dec_part;
	char *ptr;
	char *int_string = (char *)malloc(sizeof(char));
	char dec_string[32];
	int i;

	printf("\nExercise 5.2.\n");

	dec_part = strtod(n, &ptr);

   	// Split the integer part from the decimal part
	int_part = (int)dec_part;
	dec_part = dec_part - (double)int_part;

	// Build the integer part
	i = 0;
	while (int_part > 0) {
		int rem = int_part % 2;
		int_part >>= 1;
		int_string[i] = (rem ? '1' : '0');
		i++;
		int_string = (char *)realloc(int_string, (i+1) * sizeof(char));
	}

	strrev(int_string);

	// Build the decimal part
	i = 0;
	while(dec_part > 0) {
		if (i > 32) {
			printf("ERROR\n");
			return;
		}

		if (dec_part == 1) {
			dec_string[i] = '1';
			i++;
			break;
		}

		dec_part = dec_part * 2;
		if(dec_part >= 1) {
			dec_string[i] = '1';
			dec_part -= 1;
		} else {
			dec_string[i] = '0';
		}

		i++;
	}

	printf("The binary representation of %s is %s.%s\n", n, int_string, dec_string);
}

/**
 * Exercise 5.3.
 * Given an integer, print the next smallest and next largest number that have 
 * the same number of 1 bits in their binary representation.
 *
 * SOLUTION:
 * Rules:
 * - if we turn on a '0' (at position i) we need to turn off an '1' (at position j)
 *   => the number changes by 2^i - 2^j
 * - in order to get a bigger number with the same number of 1's and 0's
 *   => i must be bigger than j
 *
 * Algorithm for the biggest:
 * - traverse from right to left
 * - when an 1 is found => the next 0 becomes 1 => this increases the number by 2^i
 *   Ex: xxxxx011100 becomes 
 *   	 xxxxx111100
 * - turn off the 1 just at the right side of that => this increases the no by 2^i - 2^j
 *   Ex: xxxxx111100 becomes 
 *       xxxxx101100
 * - make the number as small as possible to rearranging the ones at the far right
 *   Ex: xxxxx101100 becomes
 *       xxxxx100011
 *
 * Algorithm for the smallest (the reverse of the above):
 * - traverse from right to left
 * - found 0 => turn off the next 1
 *   Ex: xxxxx100011 becomes
 *   	 xxxxx000011
 * - turn on the 0 directly to the right
 *   Ex: xxxxx000011 becomes
 *   	 xxxxx010011
 * - make the number as big as possible by shifting all the ones as far to the left as possible
 *   Ex: xxxxx010011 becomes
 *   	 xxxxx011100
 *
 *
 */

/*** Helpers ***/

int get_bit(int n, int i) 
{
	// return 1 if the i th bit in n is set, 0 otherwise
	return ((n & (1 << i)) > 0);
}

int set_bit(int n, int i, int b)
{
	// if b specifies to set the i th bit in n, then set it
	if(b)
		return n | (1 << i);

	// turn off the i th bit of n
	int mask = ~(1 << i);
	return n & mask;
}

/**
 * Get the next smalles number with the mentioned property.
 */
int get_next_smallest(int n)
{
	if (n <= 0)
		return -1;

	int i = 0, count_ones = 0;

	// Find the first one
	while (!get_bit(n, i))
		i++;

	// Turn on the next zero
	while(get_bit(n, i)) {
		i++;
		count_ones++;
	}
	n = set_bit(n, i, 1);

	// Turn off the the prev one
	i--;
	n = set_bit(n, i, 0);
	count_ones --;

	// Set zeros
	for(int k = i - 1; k >= count_ones; k--)
		n = set_bit(n, k, 0);

	// Set ones
	for(int k = count_ones - 1; k >= 0; k--)
		n = set_bit(n, k, 1);

	return n;	
}

/**
 * Get the previous biggest number with the mentioned property.
 */
int get_prev_biggest(int n)
{
	if (n <= 0)
		return -1;

	int i = 0, count_zeros = 0;

	// Find the first zero
	while (get_bit(n, i))
		i++;

	// Turn off the next one
	while(!get_bit(n, i)) {
		i++;
		count_zeros++;
	}
	n = set_bit(n, i, 0);

	// Turn on the the prev zero
	i--;
	n = set_bit(n, i, 1);
	count_zeros --;

	// Set ones
	for(int k = i - 1; k >= count_zeros; k--)
		n = set_bit(n, k, 1);

	// Set zeros
	for(int k = count_zeros - 1; k >= 0; k--)
		n = set_bit(n, k, 0);

	return n;	
}

void print_next_prev(int n)
{
	int sn = get_next_smallest(n);
	int bp = get_prev_biggest(n);

	printf("\nExercise 5.3.\n");
	printf("Smallest next number with the same number of 1's as n = %d is sn = %d\n", n, sn);
	printf("Biggest previous number with the same number of 1's as n = %d is bp = %d\n", n, bp);
}

/**
 * Exercise 5.5.
 *
 * Write a function to determine the number of bits required to convert integer
 * A to integer B.
 *
 * Example: 31, 14 => 2 bits
 */

/*** Helper ***/
int count_ones(int A)
{
	int count = 0;
	while(A) {
		count += (A % 2);
		A = A / 2;
	}

	return count;
}

void no_bits_to_similarity(int A, int B)
{
	int count_a = count_ones(A);
	int count_b = count_ones(B);

	printf("\nExercise 5.5.\n");
	printf("The number of bits to be changed in order to convert A = %d "
			"into B = %d is no = %d\n", A, B, abs(count_a - count_b));
}

/**
 * Exercise 5.6.
 * Swap odd and even bits in an integer with as few instructions as 
 * possible.
 *
 * E.g.: bits 0 and 1 are swapped, bits 2 and 3 are swapped, etc.
 * 
 * SOLUTION:
 * Mask all odd bits in binary: 0xAAAAAAAA 
 * and then the even bits: 0x55555555.
 */

void print_swapped_even_odd(int no)
{
	int even_on = 0x55555555;
	int odd_on = 0xAAAAAAAA;

	printf("\nExercise 5.6.\n");
	printf("After swapping the odd bits with the even bits n = %d becomes ", no);
	
	no = ((no & odd_on) >> 1) | ((no & even_on) << 1);

	printf("%d\n", no);
}

/**
 * Exercise 5.7.
 *
 * An array A[1...n] contains all the integers from 0 to n except for one number which is
 * missing. In this problem, we cannot access an entire integer in A with a single operation. 
 * The elements of A are represented in binary, and the only operation we can use 
 * to access them is “fetch the jth bit of A[i]”, which takes constant time. Write code to
 * find the missing integer. Can you do it in O(n) time?
 */
void print_missing_number(int *arr, int n, int j)
{
	int no_ones = (1 << j);
	int no_zeros = (1 << j);

	printf("zeros = %d, ones = %d\n", no_zeros, no_ones);
	printf("\nExercise 5.7.\n");
	printf("The missing number is ");

	for(int i = 0; i <= n - 1; i++) {
		if(no_zeros && ((arr[i] & (1 << j)) == 0)) {
			no_zeros -= 1;
		} else if(!no_zeros && no_ones && (arr[i] & (1 << j))) {
			no_ones -= 1;

			if (no_ones == 0) {
				no_zeros = (1 << j);
				no_ones = (1 << j);
			}	
		} else {
			printf("%d\n", i - 1);
			return;
		}
	}
}

int main(void)
{

	// Exercise 5.1.
	char N[] = "10000000000";
	char M[] = "10101";

	int i=2, j=6;

	set_bits_in_interval(N, M, i, j);

	// Exercise 5.2.
	print_binary("3.5");

	// Exercise 5.3.
	print_next_prev(13);

	// Exercise 5.5.
	no_bits_to_similarity(31, 14);

	// Exercise 5.6.
	print_swapped_even_odd(10);

	// Exercise 5.7.
	int arr[] = {0, 1, 2, 3, 4, 5, 7, 8, 9, 10};
	print_missing_number(arr, 10, 2);

	return 0;
}

