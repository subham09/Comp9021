# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children,
# - the sum of the nodes along all of T*'s branches is equal to M, and
# - when leaves in T are expanded to 2 leaves in T*, those 2 leaves receive the same value.
#
# Written by Subham Anand for COMP9021


import sys
from random import seed, randrange

from binary_tree_adt import *


def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)


def expand_tree(tree):
    if tree.value is not None:
        sum = 0
        L = tree_sums(tree, sum)
        global maxele
        maxele = max(L)
        hasPathSum(tree, maxele)
    else:
        return
    #pass
    # Replace pass above with your code

def tree_sums(root, current_sum, subtree_sums = []):
    if root.value is None :
        return True
    
    current_sum += root.value

    if root.left_node.value is not None:
        left = root.left_node
        a = set(subtree_sums)
        subtree_sums = list(a)
        subtree_sums += tree_sums(left, current_sum)
    else:
        subtree_sums.append(current_sum)
    
    if root.right_node.value is not None:
        right = root.right_node
        a = set(subtree_sums)
        subtree_sums = list(a)
        subtree_sums += tree_sums(right, current_sum)
    else:
        subtree_sums.append(current_sum)
    #print(subtree_sums)
    return subtree_sums

def hasPathSum(tree, s):
     
    # Return true if we run out of tree and s = 0 
    if tree.value is None:
        return (s == 0)
 
    else:
        ans = 0
         
        # Otherwise check both subtrees
        subSum = s - tree.value
         
        # If we reach a leaf node and sum becomes 0, then 
        # return True 
        if tree.left_node.value is None and tree.right_node.value is None:
            if subSum != 0:
                tree.right_node.insert_in_bst(int(subSum))
                tree.left_node.insert_in_bst(int(subSum))
                return True

        if tree.left_node.value is None and tree.right_node.value is not None:
            tree.left_node.insert_in_bst(subSum)

        if tree.right_node.value is None and tree.left_node.value is not None:
            tree.right_node.insert_in_bst(subSum)
 
        if tree.left_node.value is not None:
            ans = ans + hasPathSum(tree.left_node, subSum)

        if tree.right_node.value is not None:
            ans = ans + hasPathSum(tree.right_node, subSum)
        
        #print('mytree',tree.print_binary_tree())
        return ans 

# Possibly define other functions

                
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   ]
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
expand_tree(tree)
print('Here is the expanded tree:')
tree.print_binary_tree()


