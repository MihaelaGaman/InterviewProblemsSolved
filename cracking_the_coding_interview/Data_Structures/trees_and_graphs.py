
"""
Trees and Graphs
"""

class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent # used for exercise 4.5.

    def display(self):
        """
        A pretty print of the tree ---> taken from StackOverflow:
        https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python 
        """
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

"""
4.1. 

Implement a function to check if a tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree 
such that no two leaf nodes differ in distance from the root by more than one.

SOLUTION:
The difference b/w the min and max depth is the max difference that we can
get in this tree.

"""
print "Exercise 4.1."

def max_depth(root):
    if root == None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))

def min_depth(root):
    if root == None:
        return 0

    return 1 + min(min_depth(root.left), min_depth(root.right))

def is_balanced(root):
    return (max_depth(root) - min_depth(root) <= 1)

root = TreeNode(1)
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(8) 

root.display()

if is_balanced(root): 
    print("Tree is balanced") 
else: 
    print("Tree is not balanced")


# --------------------------------------------------------------------------

"""
Exercise 4.2.

Given a directed graph, design an algorithm to find out whether there is a route 
between two nodes.
"""
print
print "Exercise 4.2."

graph = {'A': ['B', 'C', 'D'], \
         'B': ['A'], \
         'C': ['E', 'F'], \
         'D': ['J', 'G'], \
         'E': ['F', 'I'], \
         'F': ['E'], \
         'G': ['H'], \
         'H': ['G'], \
         'I': ['B', 'H'], \
         'J': ['D']}
print "Graph: "
print graph

def node_accessible(graph, curr_node, node, accessible_so_far=[]):
    direct_neigh = graph[curr_node]
    print accessible_so_far
    for neigh in direct_neigh:
        if neigh == node:
            return True

        if neigh not in accessible_so_far:
            accessible_so_far.append(neigh)
            if node_accessible(graph, neigh, node, accessible_so_far):
                return True

    return False

print 'I is accessible from A:'
print node_accessible(graph, 'A', 'I') # True

print 'J is accessible from B:'
print node_accessible(graph, 'B', 'J') # False

# -----------------------------------------------------------------------

"""
Exercise 4.3.

Given a sorted (increaseing order) array, write an algorithm to create a
binary tree with minimal height.
"""

print
print "Exercise 4.3."

arr = [1, 4, 12, 15, 19, 22, 23, 24, 27, 45, 48, 49, 52, 57, 60, 63, 67, 69, 70]

print "The array given initially: ", arr

def build_tree(arr, parent=None):
    n = len(arr)
    mid = int(n/2) if n % 2 == 1 else int((n-1)/2)
    node = TreeNode(arr[mid])
    node.parent = parent # used for exercise 4.5.

    if n > 2:
        node.left = build_tree(arr[0:mid], node)

    if n > 1:
        node.right = build_tree(arr[mid + 1:n], node)

    return node

root = build_tree(arr)

print "The binary tree with minimal height:"
root.display()

# ----------------------------------------------------------------------

"""
Exercise 4.4.

Given a binary search tree, design an algorithm which creates a linked list
of all the nodes at each depth (i.e. if you have a tree with depth D, you'll
have D linked lists).

SOLUTION:
Dictionary with depth as key, and a list of nodes per each key.
We'll use the tree built above.
"""

print 
print "Exercise 4.4."
print "The tree used is displayed above (Exercise 4.3.)"

def get_list_of_layers(root, layers_dict={}, depth=0):
    if depth not in layers_dict:
        layers_dict[depth] = []

    layers_dict[depth].append(root.data)
    if root.left != None:
        get_list_of_layers(root.left, layers_dict, depth + 1)
    
    if root.right != None:
        get_list_of_layers(root.right, layers_dict, depth + 1)

    return layers_dict

layers_dict = get_list_of_layers(root)
print layers_dict


# --------------------------------------------------------------------------

"""
Exercise 4.5.

Write an algorithm to find the 'next' node (i.e. in-order successor) of a
given node in a BST where each node has a link to its parent.


SOLUTION:
Use the tree from Exercise 4.3 but modified such that we have link to the parent.

In-order traversal: visit X.left, X, X.right.
To find the successor of X:
    1. if X has a right child => the successor must be on the right side of X.
       Specifically: the left-most child should be visited in that sub-tree.

    2. else we call to P = X's parent.
        => a) if P.left == X => return P
        => b) if P.right == X => P is fully visited => cal successor(P)
"""

print
print "Exercise 4.5."

def in_order_successor(root):
    if root == None:
        return None

    if root.parent == None or root.right != None: # See 1 above (in the solution)
        p = leftmost_child(root.right)
    else:
        # Go up until we are on the left instead the right (See 2 b) in the solution)
        while root.parent != None:
            p = root.parent
            if p.left == root:
                break
            root = p
    
    return p

def leftmost_child(root):
    if root == None:
        return None

    while root.left != None:
        root = root.left

    return root

node = root.left.right.left
found = in_order_successor(node)

print "The successor of ", node.data, " is ", found.data

# --------------------------------------------------------------------------------

"""
Exercise 4.6.

Design an algorithm and write code to find the first common ancestor of two nodes in a 
binary tree. Avoid storing additional data structures.

"""
print
print "Exercise 4.6."

def find_ancestor(root, node1, node2):
    count_left = search_side(root.left, node1, node2)
    if count_left == 2:
        return find_ancestor(root.left, node1, node2)

    if count_left == 1:
        return root

    count_right = search_side(root.right, node1, node2, count_left)
    if count_left == 0 and count_right == 2:
        return find_ancestor(root.right, node1, node2)

    return None

def search_side(root, node1, node2, count=0):
    if root == node1 or root == node2:
        count += 1

    if root != None and count < 2:
        count = search_side(root.left, node1, node2, count)
        count = search_side(root.right, node1, node2, count)

    return count


node1 = root.right.left.right.right
node2 = root.right.right.right.right

ancestor = find_ancestor(root, node1, node2)
print "node1 = ", node1.data, " and node2 = ", node2.data, " have the ancestor = ", ancestor.data

# ----------------------------------------------------------------------------------------------

"""
Exercise 4.7.

You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes.
Create an algorithm to decide if T2 is a subtree of T1.

SOLUTION:
    When T2 is found in T1, continue on that path until the leaves or 
    until a mismatch is encountered.
"""
print
print "Exercise 4.7."

def contains_subtree(tree1, tree2):
    if tree2 == None:
        return True

    return subtree(tree1, tree2)

def subtree(node1, node2):
    # tree1 (the "parent") is empty and tree2 is still not found
    if node1 == None:
        return False

    if node1.data == node2.data:
        if match_tree(node1, node2):
            return True

    return subtree(node1.left, node2) or subtree(node1.right, node2)

def match_tree(node1, node2):
    if node1 == None and node2 == None:
        return True # nothing to further compare

    if node1 == None or node2 == None:
        return False # tree1 is empty and tree2 is still not found

    if node1.data != node2.data:
        return False # the data does not match

    return match_tree(node1.left, node2.left) and match_tree(node1.right, node2.right)


tree1 = root
tree2 = root.left.right

is_subtree = contains_subtree(tree1, tree2)

print "tree2 = ", tree2.data, " is subtree of tree1 = ", tree1.data, ": ", is_subtree

