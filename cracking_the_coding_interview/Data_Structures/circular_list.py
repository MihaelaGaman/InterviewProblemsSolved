
class CircularNode:
    def __init__(self, d):
        self.next = None
        self.data = d
    
    def appendToTail(self, d, circNode=None):
        end = CircularNode(d)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

        if circNode != None:
            end.next = circNode

    def findNthLast(self, N):
        """
        Find the Nth to last element.
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

    def printElems(self):
        head = self
        while head.next != None:
            print head.data, " ", 
            head = head.next
        print head.data
        print


def findBeginning(head):
    """
    PROBLEM:
    Given a circular linked list, find the beginning of the loop.

    Circular linked list: A corrupt linked list in which a node's next pointer
    points to an earlier node, so as to make a loop in the linked list.

    EXAMPLE:
    Input: A->B->C->D->E->C (the same C as earlier)
    Output: C

    SOLUTION:
    - use pointer 1 with speed 1
    - pointer 2 with speed 2
    => these will end up meeting if the linked list has a loop.
    
    Analogy: 
    Two people racing around a track, one running 2x (fast_r) as fast as the other (slow_r).
    If they start off at the same place, when will they next meet?  
        - at the start of the next lap.

    Now, let's suppose fast_r had a head start of k meters on an n step lap. 
    When  will they next meet?  
        - k meters before the start of the next lap
        - Why? fast_r would have made k + 2(n - k) steps, including its head start, and 
        - slow_r would have made n - k steps
        - both will be k steps before the start of the loop

    Now, going back to the problem, when fast_r (n2) and slow_r (n1) are moving 
    around our circular linked list, n2 will have a head start of k on the loop when n1 enters.
    Where k is the number of nodes before the loop
    => n1 and n2 will meet k nodes before the start of the loop

    So, we now know the following:
    1. Head is k nodes from LoopStart (by definition) 
    2. MeetingPoint for n1 and n2 is k nodes from LoopStart (as shown above) 

    Thus, if we move n1 back to Head and keep n2 at MeetingPoint, and move them both at the 
    same pace, they will meet at LoopStart.
    """

    n1 = head
    n2 = head

    # Find the meeting point
    while n2.next:
        n1 = n1.next
        n2 = n2.next.next
        if n1 == n2:
            break;

    # No meeting point
    if n2.next == None:
        return None

    # Move n1 to head.
    # Keep n2 at meeting point.
    # Each are k steps from the loop start.
    # If they move at the same pace, they must meet at Loop Start.
    n1 = head
    while n1 != n2:
        n1 = n1.next
        n2 = n2.next

    # Now n2 points to the start of the loop
    return n2

node = CircularNode('A')
node.appendToTail('B')
node.appendToTail('C')
node.appendToTail('D')
nth = node.findNthLast(2)
node.appendToTail('E', nth)

#print "The initial list:"
#node.printElems()
#print

print "Exercise 2.5."
print "The node at the beginning of the loop: ",
begCycl = findBeginning(node)
print begCycl.data
print
