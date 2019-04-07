#include <stdio.h>


/**
	Return x with the n bits that begin at position p inverted and the
	rest of bits unchanged.
*/

// TODO invert(x, p, n)

/**
	Return the value of the integer x rotated to the right by n positions.
*/

// TODO rightrot(x, n)

/**
	Return x with the n bits that begin at position p set to the rightmost
	n bits of y. Leave the other bits of x unchanged.	
*/
unsigned setbits(unsigned x, int p, int n, unsigned y)
{
	unsigned mask = 0;

	//mask = mask | 

  return x;
}

int bitcount(unsigned x)
{
	int b;

	for(b = 0;  x != 0; x >>= 1)
		if(x & 1)
			b++;

	return b;

}

int main()
{
	unsigned x = 12478; // 0011 0000 1011 1110
	unsigned y = 23915; // 0101 1101 0110 1011
  int p = 7, n = 6;

	// the n rightmost bits of y
	// ~0 is all ones. ~0 << n (shift left with n => 0 in the n rightmost pos)
	// ~(~0<<n) => 1 in the n rigtmost positions 
	// => a mask to get the n rightmost bits of y
	unsigned z = y & ~(~0 << n);
	// the n bits of x starting at position p
	unsigned t = (x >> (p + 1 - n)) & ~(~0 << n);

	// TODO

	printf("%u\n", t);

	return 0;
}
