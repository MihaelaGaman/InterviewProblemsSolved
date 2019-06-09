


"""
Chapter 9:
    Sorting and Searching
"""

"""
Exercise 9.1.

You are given two sorted arrays A and B.
A has a large enough buffer to hold B.
Write a method to merge B into A in sorted order.
"""

def merge_sorted(A, B):
    i = 0
    j = 0

    while j < len(B) and  B[j] <= A[i]:
        A = [B[j]] + A
        j += 1
        i += 1

    while i < len(A) - 1 and j < len(B):
        if A[i] <= B[j] and A[i+1] >= B[j]:
            A = A[:i+1] + [B[j]] + A[i+1:]
            i += 1
            j += 1
        else:
            i += 1

    while j < len(B):
        A.append(B[j])
        j += 1

    return A

A = [1, 2, 3, 21, 22, 35, 40]
B = [5, 6, 7, 22, 23, 24, 37]

print "Exercise 9.1."
print "A = ", A
print "B = ", B

A = merge_sorted(A, B)
print "A merged = ", A

"""
9.2.
Write a method to sort an array of strings so that all the anagrams are next to each other.
"""

"""
Exercise 9.3.
Given a sorted arry of n integers that has been rotated an unknown number of times, 
give a O(log n) algorithm that finds an element in the array.
You may assume that the array was originally sorted in increasing order.

EXAMPLE:
Input: find 5 in array (15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14)
Output: 8 (the index of 5 in the array)
"""

def find_elem(arr, elem, start, stop):
    if elem == arr[start]:
        return start

    if elem == arr[stop]:
        return stop

    m = int((stop - start)/2) + start

    if arr[m] == elem:
        return m

    if arr[start] > elem and elem < arr[m] or arr[start] < elem and elem < arr[m]:
        return find_elem(arr, elem, start + 1, m - 1)

    if arr[m] < elem and elem < arr[stop] or arr[m] > elem and elem < arr[stop]:
        return find_elem(arr, elem, m + 1, stop - 1)

    return "NOT FOUND"

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
elem = 5
pos = find_elem(arr, elem, 0, len(arr) - 1)

print "Exercise 9.3."
print "The position of elem = ", elem
print "in arr = ", arr
print "is pos = ", pos
print

"""
Exercise 9.4.

If you have a 2GB file with one string per line, which sorting algorithm
would you use to sort the file and why?

SOLUTION:
2GB size ---> not all the data will be brought into the memory.

Assume we have X MB of memory available, the algorithm is the one below:
1. divide the file into K chunks: X * K = 2 GB
2. bring each chunk into the memory and sort the lines as usual using any O(n log n) algorithm.
3. save the lines back to the file.
4. bring the next chunk into the memory and sort.
3. once we're done, merge them one by one. (N-WAY MERGE).

^ EXTERNAL SORT!!!
"""

"""
Exercise 9.5.

Given a sorted array of strings which is interspersed with empty strings, 
write a method to find the location of a given string.

Example: find "ball" in ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
         will return 4
Example: find "ballcar" in ["at", "", "", "", "", "ball", "car", "", "", "dad", "", ""]
         will return -1
"""

def find_string(arr, s, start, stop):
    while start < len(arr) and arr[start] == "":
        start += 1

    while stop >= 0 and arr[stop] == "":
        stop -= 1

    if start >= len(arr) or stop < 0:
        return -1

    if elem == arr[start]:
        return start

    if elem == arr[stop]:
        return stop

    m = int((stop - start)/2) + start

    if elem == arr[m]:
        return m

    pos1 = -1
    pos2 = -1
    if arr[m] == "" or arr[start] < elem and elem < arr[m]:
        pos1 = find_string(arr, s, start + 1, m - 1)

    if arr[m] == "" or arr[m] < elem and elem < arr[stop]:
        pos2 = find_string(arr, s, m + 1, stop - 1)

    return max(pos1, pos2)

arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
elem = "ball"
pos = find_string(arr, elem, 0, len(arr) - 1)

print "Exercise 9.5."
print "For array:"
print arr
print "element ", elem, " was found at pos = ", pos

arr = ["at", "", "", "", "", "ball", "car", "", "", "dad", "", ""] 
elem = "ballcar"
pos = find_string(arr, elem, 0, len(arr) - 1)

print 
print "Case 2: "
print"For array:"
print arr
print "element ", elem, " was found at pos = ", pos

"""
Exercise 9.6.

Given a matrix in which each row/column is sorted,
write a method to find an element in it.

SOLUTION:
move to left (aka col--) 
    => eliminates all the elements below the current cell in that column.
move down (aka row--) 
    => eliminates all the elements on the left of the current cell in that row.
"""

def find_in_mat(mat, elem, M, N):
    row = 0
    col = M-1

    while row < N and col >= 0:
        if mat[row][col] == elem:
            print "element ", elem, " has been found at position (", row, ", ", col, ")" 
            return row, col
        if mat[row][col] > elem:
            col -= 1
        else:
            row += 1

    print "element ", elem, " has not been found"
    return None, None

mat = [[1, 2, 3, 4], \
       [6, 8, 10, 17], \
       [7, 9, 12, 21]]

N = 3
M = 4

elem1 = 18
elem2 = 10

print "Exercise 9.6."
find_in_mat(mat, elem1, M, N)
print
find_in_mat(mat, elem2, M, N)
print

"""
Exercise 9.7.

A circus is designing a tower routine consisting of people standing atop one another's shoulders. 
For practical and aesthetic reasons, each person must be both shorter
and lighter than the person below him or her. Given the heights and weights of each
person in the circus, write a method to compute the largest possible number of 
people in such a tower.

EXAMPLE:
Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
Output: The longest tower is length 6 and includes from top to bottom: (56, 90)
(60,95) (65,100) (68,110) (70,150) (75,190)
"""

def get_heighest_tower(sizes, N):
    # STEP 1: sort by height (use weight as second criterion)
    sizes = sorted(sizes)
    restart = True
    start = 0
    longest = 0
    seq_lg = []

    # STEP 2: find the longest sequence containing increasing heights and weights
    while restart:
        prev_w = sizes[start][1]
        for i in range(start, len(sizes)):
            curr_w = sizes[i][1]
            if prev_w > curr_w:
                longest = max(longest, i - start)
                seq_lg = sizes[start:i]
                start = i
                break

        restart = False

    if longest == 0:
        longest = N
        seq_lg = sizes[0:N]

    print "The longest sequence is ", seq_lg

sizes = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
N = len(sizes)

print "Exercise 9.7."
get_heighest_tower(sizes, N)
print
