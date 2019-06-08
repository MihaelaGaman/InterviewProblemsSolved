import copy

"""
Chapter 8: Recursion
"""

"""
Exercise 8.1.

Write a method to generate nth Fibonacci number.
"""

def fibo(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)

n = 9

print("Exercise 8.1.")
print "The nth = ", n, " Fibonacci number is ", fibo(n)
print

"""
Exercise 8.2.

Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can
only move in two directions: right and down. How many possible paths are there for
the robot?

FOLLOW UP
Imagine certain squares are "off limits", such that the robot can not step on them.
Design an algorithm to get all possible paths for the robot.
"""

def paths(i, j, N, last_action=None):
    if i == N and j == N:
        return 0

    if last_action == None:
        return 2 + paths(i + 1, j, N, last_action="RIGHT") + paths(i, j + 1, N, last_action="DOWN")

    if last_action == "RIGHT":
        if i == N:
            return 1 + paths(i, j + 1, N, "DOWN")
        if j == N:
            return paths(i + 1, j, N, "RIGHT")
        
    if last_action == "DOWN":
        if i == N:
            return paths(i, j + 1, N, "DOWN")
        if j == N:
            return 1 + paths(i + 1, j, N, "RIGHT")
        
    return 1 + paths(i + 1, j, N, "RIGHT") + paths(i, j + 1, N, "DOWN")

N = 8
print "Exercise 8.2."
print "The number of paths for N = ", N, " is ", paths(1, 1, N)
print

"""
Exercise 8.3.

Write a method that returns all the subsets of a set.
"""

def all_subsets(arr):
    if not arr:
        return [arr]

    rest = all_subsets(arr[1:])

    return rest + [[arr[0]] + item for item in rest]

arr = [1, 2, 3, 4, 5, 6]
power_set = all_subsets(arr)
print "Exercise 8.3."
print "arr = ", arr
print "power set: ", power_set

"""
Exercise 8.4.

Write a method to compute all permutations of a string.
"""

def permutations(s, plist=[]):
    if s in plist:
        return plist

    plist.append(s)

    for i in range(1, len(s)):
        plist = permutations(s[i] + s[1:i] + s[0] + s[i+1:], plist)

    return plist

s = "ABC"
perms = permutations(s)

print "Exercise 8.4."
print
print "string = ", s
print "permutations = ", perms
print "... with length = ", len(perms)
print 

"""
Exercise 8.5.
Implement an algorithm to print all valid (e.g. properly opened and closed)
combinations of n-pairs parentheses.

EXAMPLE:
input: 3 (aka 3 pairs of parenteses)
output: ()()(), ()(()), (())(), ((()))
"""

def print_parentheses_combos(left, right, s, pos=0):
    if left < 0 or right < left:
        return

    # print this combo
    if left == 0 and right == 0:
        print s
    else:
        if left > 0:
            s = s[:pos] + '(' + s[pos+1:]
            print_parentheses_combos(left - 1, right, s, pos + 1)

        if right > left:
            # try a right parenthese if there is a matching left
            s = s[:pos] + ')' + s[pos + 1:]
            print_parentheses_combos(left, right - 1, s, pos + 1)

N = 3
s = ''
for i in range (2 * N):
    s += ' '
print "Exercise 8.5."
print "For N = ", N, " the following matching parentheses have been generated: "
print_parentheses_combos(N, N, s)
print

"""
Exercise 8.6.
Implement the "paint fill function tht one might see on many image editing programs.
That is, given a screen (represented by a 2-dimensional array of colors),
a point and a new color, fill in the surrouning area until you hit a border of that color.
"""

def fill_color(screen, i, j, old_c, new_c):
    if i < 0 or j < 0 or i >= len(screen) or j >= len(screen[0]):
        return False

    if screen[i][j] == old_c:
        screen[i][j] = new_c

        # fill left
        fill_color(screen, i, j - 1, old_c, new_c)

        # fill right
        fill_color(screen, i, j + 1, old_c, new_c)

        # fill up
        fill_color(screen, i - 1, j, old_c, new_c)

        # fill down
        fill_color(screen, i + 1, j, old_c, new_c)

    return True

def pretty_print(mat, M, N):
    for i in range(N):
        for j in range(M):
            print mat[i][j], " ",
        print
    print

old_c = 'R'
new_c = 'G'

N = 3
M = 4

i = 1
j = 2

screen = [[old_c for j in range(M)] for i in range(N)]

print "Exercise 8.6."
print "The screen initially:"
pretty_print(screen, M, N)

fill_color(screen, i, j, old_c, new_c)

print "The screen after the fill:"
pretty_print(screen, M, N)
print

"""
Exercise 8.7.

Given an infinite number of quarters (25 cents), dimes (10 cents),
nickels (5 cents) and pennies (1 cent), write code to calculate 
the number of ways of representing n cents.
"""

def repres_cents(N, cents, so_far=[], all_repres=[]):
    if N <= 0:
        all_repres.append(so_far)
    else:
        for c in cents:
            if c <= N:
                temp = copy.deepcopy(so_far)
                temp.append(c)
                repres_cents(N-c, cents, temp, all_repres)
    return all_repres

N = 14
cents = [1, 5, 10, 25]

all_repres = repres_cents(N, cents)

print "Exercise 8.7."
print "We can represent ", N, " cents as: "
print all_repres
print

"""
Exercise 8.8.

Write an algorithm to print all ways of arranging eight queens on a chess
board so that none of them share the same row, column or diagonal.
"""

def is_safe(mat, row, col):
    for i in range(row):
        # on the same column       
        if mat[i][col] == 'Q':
            return False

        # on the same upper left diagonal
        if row - i - 1 >= 0 and col - i - 1 >= 0 and mat[row-i-1][col-i-1] == 'Q':
            return False

        # on the same upper right diagonal
        if row - i - 1 >= 0 and col + i + 1 < len(mat) and mat[row-i-1][col+i+1] == 'Q':
            return False

    return True

count = 0
def place_queen(mat, row):
    global count
    if row == 8:
        count += 1
        print count
        pretty_print(mat, len(mat), len(mat[0]))
        print "_________________________________"

        return

    for i in range(len(mat)):
        if row == 0 or is_safe(mat, row, i):
            aux = copy.deepcopy(mat)
            aux[row][i] = 'Q'
            place_queen(aux, row + 1)

N = 8
mat = [["_" for j in range(N)] for i in range(N)]

print "Exercise 8.8."
print "Initialy:"
pretty_print(mat, N, N)

print "All the ways to arrange the queens such that they do not attack each other:"
place_queen(mat, 0)
