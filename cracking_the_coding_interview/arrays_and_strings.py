
# 1.1. ----------------------------------------------------------------------

def unique_chars(s):
    """
    Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures?
    """
    for i in range(len(s)):
        if i > 0 and s[i] in s[:(i-1)]:
            return False

    return True

s = "aaabgdf"
print "Exercise 1.1:"
print "String: ", s, "  Unique characters check: ", unique_chars(s)
print

# 1.2. ------------------------------------------------------------------------

def reverse_str(s):
    """
    Reverse a C-style string (aka "abcd" is represented as five characters, 
    including null.
    """
    s_resp = ""
    for i in range(len(s) - 2, -1, -1):
        s_resp += s[i]

    s_resp += s[len(s) - 1]

    return s_resp

s = "abcdefg\n"
print "Exercise 1.2:"
print "The reverse of string: ", s, " is: ", reverse_str(s)
print

# 1.3. ------------------------------------------------------------------------

def remove_duplicates(s):
    """
    Remove the duplicates characters in a string.
    Do not use additional buffers.
    One or two extra-variables are fine, but not an extra copy of the array.
    """
    n = len(s) - 1
    while n:
        if s[n] in s[0:n]:
            s = s[0:n] + ("" if n == len(s) - 1 else s[n+1:])
        n -= 1
        
    return s

s = "abaaaacsssbbbbaaadsp"
print "Exercise 1.3:"
print "String ", s, \
" after the duplicates have been removed: ", remove_duplicates(s)
print

# 1.4. -------------------------------------------------------------------------

def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    i = 0
    n = len(s1)
    
    while i < n:
        if s1[i] not in s2:
            return False

        j = s2.index(s1[i])
        s2 = ("" if j == 0 else s2[0:j]) + \
            ("" if j == len(s2) - 1 else s2[j+1:])

        i += 1

    return True

s1 = "anagrama"
s2 = "agramana"

print "Exercise 1.4:"
print "Strings s1 = ", s1, " and s2 = ", s2, " are anagrams: ", \
        check_anagrams(s1, s2)
print

# 1.5. ----------------------------------------------------------------------

def replace_spaces(s):
    """
    Write a method to replace all spaces in a string with %20.
    """
    i = 0
    n = len(s)

    while i < n:
        if s[i] == ' ':
            s = ("" if i == 0 else s[0:i]) + "%20" + \
                ("" if i == n - 1 else s[i+1:])
            n += 2
            i += 2
        i += 1

    return s

s = "Ana are    mere multe    ."
print "Exercise 1.5:"
print "String s = ", s, " having spaces replaced with %20: ", \
        replace_spaces(s)
print

# 1.6. ----------------------------------------------------------------

def rotate_matrix_90(mat):
    """
    Given an image represented by an NxN matrix, where each pixel in the
    image is 4 bytes, write a method to rotate the image by 90 degrees.
    Can you do this in place?
    """
    i = 0
    n = len(mat) - 1

    while i < n:
        l = i
        c = n

        while l < n and c > i:
            aux = mat[l][n]
            mat[l][n] = mat[i][l]

            aux2 = mat[n][c]
            mat[n][c] = aux

            aux = mat[c][i]
            mat[c][i] = aux2

            mat[i][l] = aux
            
            l += 1
            c -= 1

        i += 1
        n -= 1

    return mat

def print_mat(mat):
    for l in mat:
        for elem in l:
            print elem, " ",
        print

mat = [[1, 2, 3, 4, 5], \
       [6, 7, 8, 9, 10], \
       [11, 12, 13, 14, 15], \
       [16, 17, 18, 19, 20], \
       [21, 22, 23, 24, 25]]

print "Exercise 1.6:"
print "Original matrix:"
print_mat(mat)
print
print "Rotated 90 degrees:"
mat = rotate_matrix_90(mat)
print_mat(mat)
print

# 1.7. -------------------------------------------------------------------

def zeroise_mat(mat):
    """
    Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column is set to 0.
    """
    m = len(mat)
    n = len(mat[0])

    z_row = []
    z_col = []

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                z_row.append(i)
                if j not in z_col:
                    z_col.append(j)
                break

    mat = [[(mat[i][j] if i not in z_row and j not in z_col else 0) \
            for j in range(n)] for i in range(m)]

    return mat

mat = [[0, 0, 1, 2, 3, 0, 4, 5], \
       [1, 2, 0, 4, 9, 1, 2, 9], \
       [3, 9, 2, 5, 2, 1, 9, 1]]
print "Exercise 1.7:"
print "Matrix before zeroise:"
print_mat(mat)
print
print "Matrix after zeriose:"
mat = zeroise_mat(mat)
print_mat(mat)
print

# 1.8. --------------------------------------------------------------------
def isSubstring(s1, s2):
    if len(s1) < len(s2):
        return False

    if len(s1) == len(s2) and s1 != s2:
        return False
    elif s1 == s2:
        return True

    for i in range(len(s1) - len(s2)):
        if s1[i:i+len(s2)] == s2:
            return True

    return False

def str_rotation(s1, s2):
    """
    Check if s2 is a rotation of s1 using only one call to isSubstring.
    """

    if len(s1) != len(s2):
        return False

    # Concatenate s2 with itself and see if s1 is a substring of
    # the result
    s = s2 + s2
    if isSubstring(s, s1):
        return True
    
    return False

print "Exercise 1.8:"
s1 = "apple"
s2 = "pleap"
print "s1 = ", s1, " is rotation of s2 = ", s2, " : ", str_rotation(s1, s2)
print 

s1 = "apple"
s2 = "ppale"
print "s1 = ", s1, " is rotation of s2 = ", s2, " : ", str_rotation(s1, s2)
print

s1 = "waterbottle"
s2 = "erbottlewat"
print "s1 = ", s1, " is rotation of s2 = ", s2, " : ", str_rotation(s1, s2)
print

