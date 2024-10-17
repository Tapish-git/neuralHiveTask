from typing import List

#Defined a node
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    
    def createTree(self, input: List) -> Node:
        if not input:
            return None
        
        root = Node(input[0])           #Create a root node for tree   
        queue = [root]          #Putt the root node into queue, for keeping track of each level
        ptr = 1             #ptr to traverse the input list
        
        while queue and ptr < len(input):
            current = queue.pop(0)          #Make this as a parent node
            while input[ptr] is not None and ptr < len(input):
                child = Node(input[ptr])        #create a new node with value at current index in input 
                current.children.append(child)          #add a new child node to the children of current node
                queue.append(child)         #add child to queue, tp process further
                ptr += 1
            ptr += 1                #once processed all children of the current node, increment to skip the null

        return root
    