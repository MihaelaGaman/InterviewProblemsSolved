"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

"""


def longestPalindrome(s):
    max_len = 1
    start = 0; low = 0; high = 0
    n = len(s) 
  
    # Consider each character as center point of even len palindromes 
    for i in xrange(1, n): 
        # Find the longest even len palindrome with center points i-1 and i. 
        low = i - 1
        high = i 
        while low >= 0 and high < n and s[low] == s[high]: 
            if high - low + 1 > max_len: 
                start = low 
                max_len = high - low + 1
            low -= 1
            high += 1
  
        # Find the longest odd len palindrome with center point i 
        low = i - 1
        high = i + 1
        while low >= 0 and high < n and s[low] == s[high]: 
            if high - low + 1 > max_len: 
                start = low 
                max_len = high - low + 1
            low -= 1
            high += 1
  
    return s[start:start + max_len]  

 
# Test 1
s = "babad"
print "Test 1: ", s, " longest palindrome = ", longestPalindrome(s)

# Test 2
s = "cbbd"
print "Test 2: ", s, " longest palindrome = ", longestPalindrome(s)

# Test 3
s = "bbbb"
print "Test 3: ", s, " longest palindrome = ", longestPalindrome(s)

# Test 4
s = "a"
print "Test 4: ", s, " longest palindrome = ", longestPalindrome(s)

# Test 5
s = "aacdefcaa"
print "Test 5: ", s, " longest palindrome = ", longestPalindrome(s)


