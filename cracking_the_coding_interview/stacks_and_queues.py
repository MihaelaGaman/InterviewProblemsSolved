


class Node:
    def __init__(self, d):
        self.next = None
        self.data = d

    def appendToTail(self, d):
        end = Node(d)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        return None if self.top == None else self.top.data

    def pop(self):
        if self.top != None:
            item = self.top.data
            self.top = self.top.next
            return item

        return None

    def push(self, item): 
        t = Node(item)
        t.next = self.top
        self.top = t

class StackWithMin:
    def __init__(self):
        self.top = None
        self.smin = Stack() # Exercise 3.2. stack min

    def peek(self):
        return self.top.data

    def pop(self):
        if self.top != None:
            item = self.top.data
            self.top = self.top.next
            return item

        return None

    def popMin(self):
        """
        Exercise 3.2. 
        Stack with min.
        """

        print "Stack with min: pop ",
        val = self.pop()
        if val == self.minimum():
            self.smin.pop()

        print val

        return val

    def push(self, item): 
        t = Node(item)
        t.next = self.top
        self.top = t

    def pushMin(self, item):
        print "Stack with min: push ",item 
        if item < self.minimum():
            self.smin.push(item)

        self.push(item)

    def minimum(self):
        print "Stack with min: min = ", 
        if self.smin.top == None:
            return 32000

        print self.smin.peek()

        return self.smin.peek()


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        if self.first == None:
            self.last = Node(item)
            self.first = self.last
        else:
            last.next = Node(item)
            self.last = last.next

    def dequeue(n):
        if self.first != None:
            item = self.first.data
            self.first = self.first.next
            return item

        return None

"""
Exercise 3.1.
Describe how you could use a single array to implement three stacks.

Solution:
Divide the array in three equal parts and allow the individual stack to grow
in that limited space:
- for stack 1, use [0, n/3)
- for stack 2, use [n/3, 2n/3)
- for stack 3, use [2n/3, n)
"""

n = 21 
ss = int(n/3) # stack size
buf = [0 for i in range(n)]
sp = [0, 0, 0] # stack pointers to the top elem

def push(s_no, value):
    print "Push val = ", value, " into stack ", s_no
    # where are we inserting this?
    i = s_no * ss + sp[s_no] + 1
    # the top of the current stack has moved
    sp[s_no] += 1
    # add to the buffer the new value of the top elem for stack s_no
    buf[i] = value

def pop(s_no):
    print "Pop from stack ", s_no
    # what position do we actually pop from the buffer?
    i = s_no * ss + sp[s_no]
    # where will the top be after this operation?
    sp[s_no] -= 1
    # keep the value in the top (to be returned later)
    value = buf[i]
    # make zero the value of the old top of the stack
    buf[i] = 0
    return value

def peek(s_no):
    i = s_no * ss + sp[s_no]
    print "Peek val = ", buf[i], " from stack ", s_no
    return buf[i]

print "The initial buffer: "
print buf
push(0, 12)
push(0, 23)
push(1, 14)
push(2, 1)
push(1, 113)
push(2, 2)
push(2, 100)
push(0, 3)

print "The buffer after a few elements have been pushed into the stacks"
print buf

peek(0)
peek(1)
peek(2)

pop(0)
pop(1)
pop(2)

print "The buffer after a few elements have been poped"
print buf
print
print

# -----------------------------------------------------------------

"""
Exercise 3.2.
How would you design a stack which, in addition to push and pop, also has a function 
min which returns the minimum element? Push, pop and min should all operate in 
O(1) time.
"""

s = StackWithMin()
s.pushMin(14)
s.pushMin(23)
s.pushMin(12)
s.pushMin(3)
s.pushMin(1)
s.pushMin(2)

print

# -------------------------------------------------------------------

"""
Exercise 3.3. 
Imagine a (literal) stack of plates.
If the stack gets too high, it might topple. Therefore, in real life,
we would likely start a new stack when the previous stack exceeds 
some threshold.

Implement a data structure SetOfStacks that mimics this SetOfStacks
should be composed of several stacks, and should create a new stack once 
the previous one exceeds capacity SetOfStacks push() and SetOfStacks
pop() should behave identically to a single stack (that is, pop() should 
return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific 
sub-stack.
""" 

class SetOfStacks:
    def __init__(self, capacity):
        print "Build Set Of Stacks of capacity = ", capacity, " per stack"
        self.stacks_arr = []
        self.capacity = capacity
        self.total = capacity

    def push(self, item):
        print "Push Set Of Stacks, item = ", item
        n = len(self.stacks_arr)
        if n == 0 or self.total == 0:
            st = Stack()
            st.push(item)
            self.stacks_arr.append(st)
            self.total = self.capacity - 1
        else:
            self.stacks_arr[n-1].push(item)
            self.total-=1

    def pop(self):
        n = len(self.stacks_arr)
        if n == 0:
            print "Pop Set Of Stacks: None"
            return None
        item = self.stacks_arr[n-1].pop()
        
        if self.stacks_arr[n-1].peek() == None:
            self.stacks_arr.remove(self.stacks_arr[n-1])
            self.total = self.capacity

        print "Pop Set Of Stacks: ", item
        return item

    def peek(self):
        n = len(self.stacks_arr)
        if n == 0:
            print "Peek Set Of Stacks: None"
            return None
        
        print "Peek Set Of Stacks: ", self.stacks_arr[n-1].peek()
        return self.stacks_arr[n-1].peek()

print "Exercise 3.3."
sos = SetOfStacks(3)
sos.push(12)
sos.push(11)
sos.push(1)
sos.push(3)
sos.peek()
sos.push(10)
sos.pop()
sos.pop()
sos.peek()
sos.push(100)
sos.peek()

# ------------------------------------------------------------------------
"""
Exercise 3.4.

In the classic problem of the Towers of Hanoi, you have 3 rods and N disks 
of different sizes which can slide onto any tower. The puzzle starts with 
disks sorted in ascending order of size from top to bottom 
(e.g. each disk sits on top of an even larger one).
You have the following constraints: 
(A) Only one disk can be moved at a time.
(B) A disk is slid off the top of one rod onto the next rod.
(C) A disk can only be placed on top of a larger disk.

Write a program to move the disks from the first rod to the last using Stacks.
"""
A = Stack()
B = Stack()
C = Stack()

no = 10

for i in range(no, -1, 0):
    A.push(i)


# TODO
