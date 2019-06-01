


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
    def __init__(self, name=""):
        self.top = None
        self.name = name

    def peek(self, prt=False):
        if prt == True:
            print "Stack ", self.name, " peek: ", (None if self.top == None else self.top.data)

        return None if self.top == None else self.top.data

    def pop(self, prt=False):
        if prt == True:
            print "Stack ", self.name, " pop: ", (None if self.top == None else self.top.data)

        if self.top != None:
            item = self.top.data
            self.top = self.top.next
            return item

        return None

    def push(self, item, prt=False):
        if prt == True:
            print "Stack ", self.name, " push: ", item

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

print 
print "Exercise 3.1."

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
print
print "Exercise 3.2."
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

print
print "Exercise 3.4."
A = Stack(name="A")
B = Stack(name="B")
C = Stack(name="C")

no = 10

for i in range(no, -1, -1):
    A.push(i, True)

"""
SOLUTION from tutorialspoint.com

START
Procedure Hanoi(disk, source, dest, aux)

   IF disk == 1, THEN
      move disk from source to dest
   ELSE
      Hanoi(disk - 1, source, aux, dest)     // Step 1
      move disk from source to dest          // Step 2
      Hanoi(disk - 1, aux, dest, source)     // Step 3
   END IF

END Procedure
STOP

"""
def Hanoi(disk, src, dest, aux):
    if disk == 1:
        d = src.pop()
        dest.push(d)
    else:
        Hanoi(disk - 1, src, aux, dest)
        d = src.pop()
        dest.push(d)
        Hanoi(disk - 1, aux, dest, src)

print
print "Moving begins..."
Hanoi(11, A, C, B)

while C.peek() != None:
    C.pop(prt=True)

# -------------------------------------------------------------------

"""
3.5.

Implement MyQueue class which implements a queue using 2 stacks.
"""
print
print "Exercise 3.5."


class MyQueue:
    def __init__(self):
        self.s1 = Stack(name="s1") # holds the oldest elements (accessed at enqueue)
        self.s2 = Stack(name="s2") # holds the head (accessed at dequeue)

    def enqueue(self, elem):
        self.s1.push(elem, prt=True)
    
    def dequeue(self):
        if self.s2.peek() == None:
            # Refill the head
            while self.s1.peek() != None:
                self.s2.push(self.s1.pop())

        return self.s2.pop(prt=True)

    def peek(self):
        if self.s2.peek() == None:
            # Refill the head
            while self.s1.peek() != None:
                self.s2.push(self.s1.pop())

        return self.s2.peek(prt=True)

q = MyQueue()
q.enqueue(1)
q.enqueue(12)
q.enqueue(23)
q.enqueue(5)
q.dequeue()
q.peek()
q.enqueue(123)
q.dequeue()
q.dequeue()
q.enqueue(36)
q.dequeue()
q.enqueue(30)
q.dequeue()
q.peek()

# -----------------------------------------------------------

"""
Exercise 3.6.

Write a program to sort a stack in ascending order.
"""
print
print "Exercise 3.6."

l = [1, 12, 23, 5, 123, 36, 30]
stack = Stack("initial")

for elem in l:
    stack.push(elem, prt = True)

print

def sort_stack(stack):
    aux_stack = Stack("sorted")

    while stack.peek() != None:
        tmp = stack.pop()
        while aux_stack.peek() != None and aux_stack.peek() > tmp:
            aux_tmp = aux_stack.pop()
            stack.push(aux_tmp)
        aux_stack.push(tmp)

    return aux_stack

asc_stack = sort_stack(stack)
while asc_stack.peek():
    asc_stack.pop(prt=True)

