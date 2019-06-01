

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

    def removeDuplicates(self):
        """
        Exercise 2.1.
        Remove duplicates from list.
        """
        vals_so_far = []
        n = self
        while n.next != None:
            if n.data not in vals_so_far:
                vals_so_far.append(n.data)

            if n.next and n.next.data in vals_so_far:
                n.next = n.next.next
            else:
                n = n.next

    def removeDuplicates2(self):
        """
        Exercise 2.1. 
        Remove duplicates from list without using an additional buffer.

        Solution:
        Keep 2 pointers: current - does a normal iteration.
                         runner - iterates through prior nodes to check for duplicates.
                         (one duplicate per node because the previous ones have already been 
                          removed if they existed).
        """
        if self == None:
            return

        prev = self
        curr = prev.next

        while curr != None:
            runner = self
            while runner != curr: # Check for earlier duplicates
                if runner.data == curr.data: 
                    tmp = curr.next # remove current
                    prev.next = tmp
                    curr = tmp
                    break # the other duplicates have been removed

                runner = runner.next 
 
            if runner == curr: # curr node not update. Do it now.
                prev = curr
                curr = curr.next

    def findNthLast(self, N):
        """
        2.2. Find the Nth to last element.
        """
        curr = self
        while curr:
            test = curr
            aux = N 
            while aux and test:
                test = test.next
                aux -= 1

            if aux == 0 and test == None:
                return curr
            curr = curr.next
        
        return None

    def deleteNode(self, node):
        """
        Exercise 2.3:
        Delete a node in the middle of the list given access 
        only to that node.
        
        Solution:Copy th data from the next node into this node
        then delete the next node.

        Trick:
        The node cannot be deleted if it is the last one.
        """
        if node == None or node.next == None:
            return False

        nnext = node.next
        node.data = nnext.data
        node.next = nnext.next

        return True

    def printElems(self):
        head = self
        while head.next != None:
            print head.data, " ", 
            head = head.next
        print head.data
        print

def sumLinkedLists(node1, node2):
    """
    Exercise 2.4:
    You have two numbers represented by a linked list, where each node contains 
    a single digit. The digits are stored in reverse order, 
    such that the 1's digit is at the head of the list.
    Write a function that adds the two numbers and returns the sum as a linked 
    list.
    EXAMPLE 
    Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
    Output: 8 -> 0 -> 8
    """
    s = 0
    i = 1

    res = None

    while node1 != None or node2 != None:
        if node1:
            s += i*node1.data
            node1 = node1.next

        if node2:
            s += i*node2.data
            node2 = node2.next

        i *= 10

    res = Node(s%10)
    s = int(s / 10)
    while s:
        res.appendToTail(s%10)
        s = int(s/10)

    return res

node = Node(10)
node.appendToTail(1)
node.appendToTail(12)
node.appendToTail(12)
node.appendToTail(10)
node.appendToTail(2)
node.appendToTail(3)
node.appendToTail(12)
node.appendToTail(10)
node.appendToTail(1)

print "The initial list:"
node.printElems()
print

print "Exercise 2.4."
node1 = Node(3)
node1.appendToTail(1)
node1.appendToTail(5)
print "First number (list representation from right to left):"
node1.printElems()
node2 = Node(5)
node2.appendToTail(9)
node2.appendToTail(2)
print "Second number (list representation from right to left):"
node2.printElems()
nodeRes = sumLinkedLists(node1, node2)
print "Sum of the two numbers, represented as list:"
nodeRes.printElems()
print


nth = node.findNthLast(3)
print "Exercise 2.2."
print "Nth last node: ", nth.data
print

print "Exercise 2.3."
print "Remove nth last node:"
node.deleteNode(nth)
node.printElems()
print

print "Exercise 2.1."
print "Duplicates removed:"
node.removeDuplicates2()
node.printElems()
print
